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
] 


