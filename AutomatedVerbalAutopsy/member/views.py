from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.views.decorators.csrf import csrf_protect
from django.views import View
from django.urls import reverse
import requests
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
import uuid
from .models import Profile
import json
from .helpers import send_forget_password_mail

class Login_view(View):
    def get(self, request):
        return render(request, 'questionnaire/registration/login.html')
    
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
           
        if username and password:
            user= auth.authenticate(username=username, password=password)
            email = user.email
            first_name = user.first_name
            last_name = user.last_name
            
            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, 'Welcome back, ' +user.username +
                                     ' you are now logged in')
                    return redirect('questionnaire:submit_form', message='success')
                messages.error(request,'Your account is not active')
               
            else:
                messages.error(request, 'Invalid credentials, please try again')
           
        else:    
             messages.error(request, 'You do not have an account')
        # return render(request, 'registration/login.html')
        return redirect('member:login')
    



class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'You have been logged out.')
        return redirect('member:login')


    
def forgetPassword(request):
    try:
        if request.method == 'POST':
           username=request.POST.get('username')
            
           if not User.objects.filter(username=username).first():
               messages.error(request,'No user found with this email account')
               return redirect('member:forget-password')
               
           user_obj=User.objects.get(username=username)
           token= str(uuid.uuid4() )
           send_forget_password_mail(user_obj, token)
           messages.success(request,'An email is sent')
           return redirect('member:forget-password')
           

    except Exception as e:
        print(e)
    return render(request, 'questionnaire/registration/forget_password.html')

def changePassword(request, token):
    contex={}
    try:
       profile_obj = Profile.objects.get(forget_password_token = token)
       print(profile_obj)

    except Exception as e:
        print(e)
    return render(request, 'questionnaire/registration/login.html')
    # return render(request, 'questionnaire/registration/change_password.html



    
def password_reset_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)
            
            # Generate a unique token for the password reset link
            token = default_token_generator.make_token(user)
            
            # Construct the password reset link
            reset_link = request.build_absolute_uri(
                reverse('password_reset_confirm', args=[user.pk, token]))
            
            # Send the password reset email using Sendinblue API
            sendinblue_data = {
                'sender': {
                    'name': 'Elisha Massawe',
                    'email': 'elishaellyclif@gmail.com'
                },
                'to': [{'email': email}],
                'subject': 'Reset your password',
                'htmlContent': f'Click the following link to reset your password: {reset_link}'
            }
            response = requests.post(
                'https://api.sendinblue.com/v3/smtp/email',
                json=sendinblue_data,
                headers={'api-key': 'z0isodl2wljeuwq4w8oz3udqqp3qdon3'}
            )
            
            if response.status_code == 201:
                return render(request, 'questionnaire/registration/forget_password.html')
    else:
        form = PasswordResetForm()
    
    return render(request, 'questionnaire/registration/forget_password.html', {'form': form})
