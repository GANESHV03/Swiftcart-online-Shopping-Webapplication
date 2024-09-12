from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models here.
class signup(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

