from django.urls import path
from. import views
from django.contrib import messages
from django.urls import path
from .views import COD





urlpatterns = [
     path('submit-form/', views.cod, name='submit_form'),
      path('submit-form/<str:message>/', views.cod, name='submit_form'),


    # path('Questionnaire1/', views.mhanga, name='Questionnaire1'),
    # path('success/Questionnaire1/', views.success, name='success'),
    # path('Questionnaire1/<str:message>/', views.mhanga, name='Questionnaire1'),

    # path('Questionnaire2/', views.uchunguzi, name='Questionnaire2'),
    # path('Questionnaire2/<str:message>/', views.uchunguzi, name='Questionnaire2'),

     path('maelezo/', views.maelezo, name='maelezo'),
     path('maelezo/<str:message>/', views.maelezo, name='maelezo'),
    
] 


