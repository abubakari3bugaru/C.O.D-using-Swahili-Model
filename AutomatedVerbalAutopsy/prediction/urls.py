from django.urls import path
from . import views

app_name = 'prediction'
urlpatterns = [
    path('', views.index, name='index'),
    path('predict/', views.predict_disease, name='predict'),
    path('success/', views.success, name='success'),
    path('save/', views.save_questionnaire, name='save'),
    # path('questionnaire/', views.save, name='questionnaire'),
    # path('predict/result/', views.predict_result, name='predict_result'),  # Updated URL pattern
    path('badili/', views.delete_questionnaire, name='badili'),
    path('ripoti/', views.generate_report, name='ripoti'),
]
