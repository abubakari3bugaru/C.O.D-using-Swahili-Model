
from. views import Login_view,LogoutView
from django.urls import path
from .views import changePassword,forgetPassword
from django.views.decorators.csrf import csrf_exempt

app_name = 'member'

urlpatterns = [
    path('login/', Login_view.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('forget_password/', forgetPassword, name='forget-password'),
    path('change_password/<token>/', changePassword, name='change-password'),
]
