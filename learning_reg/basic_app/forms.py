from django import forms
from django.contrib.auth.models import User
from . import models
class UI(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('first_name','last_name','email','username','password')

class UI2(forms.ModelForm):
    class Meta:
        model=models.UserInfo
        fields=('profile_pic','portfolio_link')