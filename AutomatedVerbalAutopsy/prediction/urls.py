from django.urls import path
from . import views

app_name = 'prediction'
urlpatterns = [
    path('', views.index, name='index'),
    path('predict/', views.predict, name='predict'),
    path('save/', views.save_questionnaire, name='save'),
    path('back/last/', views.delete_questionnaire, name='back'),
]
