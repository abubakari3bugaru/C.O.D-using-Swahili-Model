from django.urls import path
from. import views 
from django.contrib import messages
from django.views.defaults import permission_denied


handler403 = 'questionnaire.views.permission_denied_view'



app_name = 'questionnaire'

urlpatterns = [
     path('submit-form/', views.cod, name='submit_form'),
     path('submit-form/<str:message>/', views.cod, name='submit_form'),
     path('dashboard/', views.dashboard, name='dashboard'),
     path('profile/', views.profile, name='profile'),
     path('Updated-profile/', views.Updated_profile, name='Updated_profile'),
     path('update-profile/', views.updateProfile, name='update_profile'),
     path('change-password/', views.change_password, name='change_password'),
     path('password/', views.password, name='password'),
     path('ondoa_sababu/<int:marehemu_id>/', views.ondoa, name='ondoa_sababu'),
     path('badili_sababu/<int:marehemu_id>/', views.badili_sababu, name='badili_sababu'),
     # path('search/', views.search_marehemu, name='search_marehemu'),
]



