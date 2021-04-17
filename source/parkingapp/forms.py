from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
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
        # exclude = ('password1','password2')

class UpdatePassword(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('','password1','password2')