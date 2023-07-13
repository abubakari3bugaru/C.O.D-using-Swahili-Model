from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.contrib import messages
from django.contrib import auth
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth import update_session_auth_hash
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Shuhuda,Marehemu,Sababu
from django.shortcuts import render, redirect, get_object_or_404
import plotly.graph_objects as go
from django.db.models import Count
from django.contrib.auth.decorators import user_passes_test

def group_check(user):
    return user.groups.filter(name='interviewer').exists()

def permission_denied_view(request, exception):
    return render(request, 'questionnaire/permission_denied.html', status=403)



@login_required
def cod(request, message=None):
    email=request.user.email
    username = request.user.username  # Get the authenticated user's username
    if request.method == 'POST':
            formShuhuda = Shuhuda(
                first_name=request.POST['firstName'],   
                middle_name=request.POST['middleName'],  
                last_name=request.POST['lastName'],  
                place=request.POST['place'],
                region=request.POST['region'],
                simu=request.POST['simu'],
                uhusiano=request.POST['uhusiano'],
                uhusiano_kipindi_kifo=request.POST['uhusiano_kipindi_kifo'],
            )

            formMarehemu= Marehemu(
                jina_kwanza=request.POST['jina_kwanza'],
                jina_pili=request.POST['jina_pili'],
                jina_mwisho=request.POST['jina_mwisho'],
                jinsia=request.POST['jinsia'],
                ndoa=request.POST['ndoa'],
                kuzaliwa=request.POST['kuzaliwa'],  
                kufa=request.POST['kufa'], 
                mahali=request.POST['mahali'],
                maelezo=request.POST['maelezo']
            )
            formShuhuda.save()
            formMarehemu.save()
            

            return redirect('prediction:predict')
    
    return render(request, 'questionnaire/form.html', {'username': username, 'message': message})


@login_required
def dashboard(request):
    username = request.user.username 
    sababu_values = Sababu.objects.all().order_by('-id')
    marehemu_values = Marehemu.objects.select_related('sababu').prefetch_related('shuhuda').order_by('-id')
    search_query = request.GET.get('query')
    if search_query:
      marehemu_values = marehemu_values.filter(jina_kwanza__icontains=search_query)

    paginator = Paginator(marehemu_values, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    sababu_counts = Sababu.objects.annotate(count=Count('sababu'))
    labels = [sababu.sababu for sababu in sababu_counts]
    values = [sababu.count for sababu in sababu_counts]
    plot_data = {'labels': labels, 'values': values}

    combined_data = {
        'sababu_values': sababu_values,
        'marehemu_values': page_obj,  
        'plot_data':plot_data,
        'username':username
    }
    return render(request, 'questionnaire/dashboard.html', {'combined_data': combined_data})

@user_passes_test(lambda user: user.groups.filter(name='physician').exists(), login_url='permission_denied')
def ondoa(request, marehemu_id):
    marehemu = get_object_or_404(Marehemu, id=marehemu_id)
    sababu_to_delete = marehemu.sababu
    marehemu_to_delete=marehemu
    if request.method == 'POST':
        sababu_to_delete.delete()
        marehemu_to_delete.delete()
        
        return redirect('questionnaire:dashboard')
    context = {
        'object_to_delete': marehemu_to_delete,
        'sababu_to_delete':sababu_to_delete,
    }
    return render(request, 'questionnaire/delete.html', context)

@user_passes_test(lambda user: user.groups.filter(name='physician').exists(), login_url='permission_denied')
def badili_sababu(request, marehemu_id):
    marehemu = get_object_or_404(Marehemu, id=marehemu_id)
    sababu_to_modify = marehemu.sababu
    if request.method == 'POST':
        new_sababu = request.POST.get('new_sababu')
        sababu_to_modify.sababu = new_sababu
        sababu_to_modify.save()
        return redirect('questionnaire:dashboard')
    context = {
        'object_to_modify': sababu_to_modify,
    }
    return render(request, 'questionnaire/edit.html', context)


  
@login_required
def profile(request,message=None):
     username = request.user.username 
     email=request.user.email
     first_name =request.user.first_name
     last_name = request.user.last_name
     return render(request, 'questionnaire/profile.html',{'username': username, 'message': message, 'email':email,'first_name':first_name,'last_name':last_name})


@login_required
def change_password(request):
    username = request.user.username 
    email=request.user.email
    if request.method == 'POST':
        current_password = request.POST['currentPassword']
        new_password = request.POST['newPassword']
        confirm_password = request.POST['confirmPassword']
        if request.user.check_password(current_password):
            if new_password == confirm_password:
                request.user.set_password(new_password)
                request.user.save()
                update_session_auth_hash(request, request.user) 
                messages.success(request, 'Password changed successfully.')
            else:
                messages.error(request, 'New password and confirmation password do not match.')
        else:
            messages.error(request, 'Incorrect current password.')

    return redirect('/questionnaire/profile')  


def password(request):
    username = request.user.username
    first_name =request.user.first_name
    last_name = request.user.last_name 
    return render(request, 'questionnaire/change_password.html')

def updateProfile(request,message=None):
    username = request.user.username 
    return render(request, 'questionnaire/update_profile.html')

def Updated_profile(request, message=None):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        user = request.user
        user.username = username
        user.email = email
        user.save()
        messages.success(request, 'Your profile has been updated successfully.')
        return redirect('questionnaire:profile')
    else:
        username = request.user.username
        email = request.user.email
        return render(request, 'questionnaire/profile.html', {'username': username, 'message': message,
                                                              'email': email })
