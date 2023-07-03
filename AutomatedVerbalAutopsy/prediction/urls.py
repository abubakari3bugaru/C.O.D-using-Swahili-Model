from django.urls import path
from . import views

app_name = 'prediction'
urlpatterns = [
    # path('', views.index, name='index'),
    path('predict/', views.predict_disease, name='predict'),
    path('success/', views.success, name='success'),
    path('badili/', views.delete_questionnaire, name='badili'),
    path('download/<int:marehemu_id>/', views.download_report, name='download_report'),
    path('report/', views.report, name='report'),
]
