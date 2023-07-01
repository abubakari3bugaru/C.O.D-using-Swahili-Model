from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .models import Shuhuda,Marehemu,Sababu




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

def maelezo(request, message=None):
    email=request.user.email
    all_maelezo = Marehemu.objects.all()
    paginator = Paginator(all_maelezo, 10)  # Display 10 items per pag
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    row_count = Marehemu.objects.count()
    username = request.user.username 
    return render(request, 'questionnaire/dashboard.html', {'page_obj': page_obj, 'username': username, 'row_count': row_count})


# def dashboard(request, message=None):
#     username = request.user.username
#     cod_data = CODWithSababu.objects.all()
#     cod_values = []

#     for cod_with_sababu in cod_data:
#         cod_values.append({
#             'jina_kwanza': cod_with_sababu.jina_kwanza,
#             'jina_pili': cod_with_sababu.jina_pili,
#             'jina_mwisho': cod_with_sababu.jina_mwisho,
#             'place': cod_with_sababu.place,
#             'mahali': cod_with_sababu.region,
#             'maelezo': cod_with_sababu.maelezo,
#             'sababu': cod_with_sababu.sababu,
#         })

#     return render(request, 'questionnaire/dashboard.html', {'cod_data': cod_values, 'username': username})

def dashboard(request):
    # Retrieve the latest CODWithSababu object and its associated COD object
    cod=Marehemu.objects.latest('id')
    cod_with_sababu = Sababu.objects.latest('id')
    cod = cod_with_sababu.cod
    
    # Retrieve the desired fields from both models
    jina_kwanza = cod.jina_kwanza
    jina_pili = cod.jina_pili
    jina_mwisho = cod.jina_mwisho
    place = cod.place
    region = cod.region
    maelezo = cod.maelezo
    sababu = cod_with_sababu.sababu
    
    # Prepare the data to pass to the template
    data = {
        'jina_kwanza': jina_kwanza,
        'jina_pili': jina_pili,
        'jina_mwisho': jina_mwisho,
        'place': place,
        'region': region,
        'maelezo': maelezo,
        'sababu': sababu,
    }
    
    return render(request, 'questionnaire/dashboard.html', data)    

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

        # Check if the current password matches the user's actual password
        if request.user.check_password(current_password):
            # Check if the new password and confirmation password match
            if new_password == confirm_password:
                # Update the user's password
                request.user.set_password(new_password)
                request.user.save()
                update_session_auth_hash(request, request.user)  # Important for keeping the user logged in
                messages.success(request, 'Password changed successfully.')
            else:
                messages.error(request, 'New password and confirmation password do not match.')
        else:
            messages.error(request, 'Incorrect current password.')

    return redirect('/questionnaire/profile')  # Redirect to the user's profile page

def password(request):
    username = request.user.username 
    return render(request, 'questionnaire/change_password.html')

def updateProfile(request,message=None):
    username = request.user.username 
    return render(request, 'questionnaire/update_profile.html')

def Updated_profile(request, message=None):
    if request.method == 'POST':
        # Get the updated information from the form
        username = request.POST['username']
        email = request.POST['email']

        # Update the user's profile with the new information
        user = request.user
        user.username = username
        user.email = email
        user.save()

        # Add a success message
        messages.success(request, 'Your profile has been updated successfully.')

        # Redirect the user back to the profile page
        return redirect('questionnaire:profile')

    else:
        # Retrieve the user's current information
        username = request.user.username
        email = request.user.email


        return render(request, 'questionnaire/profile.html', {'username': username, 'message': message,
                                                              'email': email })
