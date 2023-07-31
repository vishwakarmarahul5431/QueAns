from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields='__all__'
            # ['first_name','last_name','email','username','password1','password2']