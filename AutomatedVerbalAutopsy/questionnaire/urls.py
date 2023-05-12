from django.urls import path
from . import views

app_name = 'questionnaire'
urlpatterns = [
    path('', views.index, name='index'),
]
from django.urls import path
from. import views
from django.contrib import messages
from django.urls import path
from .views import mhanga





urlpatterns = [
     path('submit-form/', views.shuhuda, name='submit_form'),
      path('submit-form/<str:message>/', views.shuhuda, name='submit_form'),


    path('Questionnaire1/', views.mhanga, name='Questionnaire1'),
    path('success/Questionnaire1/', views.success, name='success'),
    path('Questionnaire1/<str:message>/', views.mhanga, name='Questionnaire1'),

    path('Questionnaire2/', views.uchunguzi, name='Questionnaire2'),
    path('Questionnaire2/<str:message>/', views.uchunguzi, name='Questionnaire2'),

     path('dashboard/', views.dashboard, name='dashboard'),
     path('dashboard/<str:message>/', views.dashboard, name='dashboard'),

    path('dashboardMhanga/', views.dashboardMhanga, name='dashboardMhanga'),
    path('dashboardMhanga/<str:message>/', views.dashboardMhanga, name='dashboardMhanga'),

    path('dashboardUchunguzi/', views.dashboardUchunguzi, name='dashboardUchunguzi'),
    path('dashboardUchunguzi/<str:message>/', views.dashboardUchunguzi, name='dashboardUchunguzi'),

] 

