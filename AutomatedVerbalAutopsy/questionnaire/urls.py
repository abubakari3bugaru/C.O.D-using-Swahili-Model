from django.urls import path
from. import views
from django.contrib import messages
from django.urls import path
from .views import COD



app_name = 'questionnaire'

urlpatterns = [
     path('submit-form/', views.cod, name='submit_form'),
     path('submit-form/<str:message>/', views.cod, name='submit_form'),
      
     path('dashboard/', views.dashboard, name='dashboard'),
     path('dashboard/<str:message>/', views.dashboard, name='dashboard'),
     path('maelezo/', views.maelezo, name='maelezo'),
     path('profile/', views.profile, name='profile'),
     path('Updated-profile/', views.Updated_profile, name='Updated_profile'),
     path('update-profile/', views.updateProfile, name='update_profile'),
     path('change-password/', views.change_password, name='change_password'),
     path('password/', views.password, name='password'),
] 


