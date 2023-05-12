
from. views import Login_view,UsernameValidationView,LogoutView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('login/', Login_view.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('validate-username/', csrf_exempt(UsernameValidationView.as_view()), name='username'),
]