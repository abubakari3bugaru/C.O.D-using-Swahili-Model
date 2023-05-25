from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.views.decorators.csrf import csrf_protect
from django.views import View
from django.urls import reverse
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from django.http import JsonResponse
from django.contrib import auth
import json

class Login_view(View):
    def get(self, request):
        return render(request, 'questionnaire/registration/login.html')
    
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
           
        if username and password:
            user= auth.authenticate(username=username, password=password)
            
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


            
class UsernameValidationView(View):
    def post(self, request):
        data= json.loads(request.body)
        username=data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error':'username should only contain alphanumeric character'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error':'username is already exist in the database'}, status=409)
        
        return JsonResponse({'username_valid':True})

class RegistrationView(View):
    def get(self,request):
        return render(request, 'registration/login.html') 
