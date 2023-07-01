
from. views import LoginView,LogoutView,RegisterView
from django.urls import path
from .views import changePassword,forgetPassword,password_reset_view
from django.views.decorators.csrf import csrf_exempt

app_name = 'member'

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('register/<str:message>/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('forget_password/', password_reset_view, name='forget-password'),
    path('change_password/<token>/', changePassword, name='change-password'),
]
