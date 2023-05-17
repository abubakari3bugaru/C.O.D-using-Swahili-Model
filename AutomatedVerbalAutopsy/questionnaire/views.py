from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.contrib import messages
from django.contrib import auth
from .models import COD
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect





@login_required
# def shuhuda(request, message=None):
#     username = request.user.username  # Get the authenticated user's username
#     if request.method == 'POST':
#         form = SubmitForm(request.POST)
#         if form.is_valid():
#             #Form data is valid, process it here
#             form_data = Shuhuda(
              
#             # Save the form data to the database
#             form_data.save()

#             return render(request, 'form1.html')  # Render a success page after form submission
#     else:
#         form = SubmitForm()
#     return render(request, 'form.html', {'username': username, 'message': message, 'form': form})

def cod(request, message=None):
    username = request.user.username  # Get the authenticated user's username
    if request.method == 'POST':
        # form = SubmitForm1(request.POST)
        # if form.is_valid():
            form_COD = COD(
                first_name=request.POST['firstName'],   # correction: firstName
                middle_name=request.POST['middleName'],  # correction: middleName
                last_name=request.POST['lastName'],  # correction: lastName
                place=request.POST['place'],
                region=request.POST['region'],
                shahidi=request.POST['shahidi'],
                simu=request.POST['simu'],
                uhusiano=request.POST['uhusiano'],
                uhusiano_kipindi_kifo=request.POST['uhusiano_kipindi_kifo'],
                jina_kwanza=request.POST['jina_kwanza'],
                jina_pili=request.POST['jina_pili'],
                jina_mwisho=request.POST['jina_mwisho'],
                jinsia=request.POST['jinsia'],
                ndoa=request.POST['ndoa'],
                kuzaliwa=request.POST['kuzaliwa'],  # correction: kuzaliwa_year
                kufa=request.POST['kufa'],  # kufa_year
                mahali=request.POST['mahali'],
                maelezo=request.POST['maelezo']
            )
            form_COD.save()
            return redirect('maelezo')
    
    return render(request, 'form.html', {'username': username, 'message': message})


#function ya kuingiza data to database kwa mhanga


def maelezo(request,message=None):
    all_maelezo=COD.objects.order_by('-id').values_list('maelezo', flat=True).first()
    # row_count = all_maelezo.count()
    
    username = request.user.username 
    return render(request, 'success.html',{'all_maelezo': all_maelezo, 'username': username,})

