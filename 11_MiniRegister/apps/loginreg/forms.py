from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class LoginForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=100, widget=forms.PasswordInput)
