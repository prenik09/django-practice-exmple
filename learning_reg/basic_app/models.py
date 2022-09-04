from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    # additional fields
    profile_pic=models.ImageField(upload_to='profile_pic',blank=True)
    portfolio_link=models.URLField(blank=True)