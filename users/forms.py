from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from.models import Profile


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=10)
    first_name = forms.CharField(max_length=12)
    last_name = forms.CharField(max_length=12)
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=12)
    last_name = forms.CharField(max_length=12)
    about = forms.Textarea()
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email']


class ProfileUpdateForm(forms.ModelForm):
        
    class Meta:
        model = Profile
        fields = ['image']