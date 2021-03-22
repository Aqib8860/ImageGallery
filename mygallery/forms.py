from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import forms
from django.forms import ModelForm
from .models import *


class UserRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']


class UserLogin(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class AddImage(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
