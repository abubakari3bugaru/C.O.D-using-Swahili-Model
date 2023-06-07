from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User ,on_delete=models.CASCADE)
    forget_pass_token=models.CharField(max_length=100)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username