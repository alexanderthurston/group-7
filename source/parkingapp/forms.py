from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

class UserCreationFormExtended(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')
