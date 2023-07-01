from django.urls import path
from . import views

app_name = 'prediction'
urlpatterns = [
    path('', views.index, name='index'),
    path('predict/', views.predict_disease, name='predict'),
    path('success/', views.success, name='success'),
    path('badili/', views.delete_questionnaire, name='badili'),
    path('ripoti/', views.generate_report, name='ripoti'),
]
