from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your Username",
                "class": "form-input",
                "id": "LoggingEmailAddress"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter your Password",
                "class": "form-input",
                "id": "loggingPassword"
            }
        ))

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-input",
                "id": "LoggingEmailAddress"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-input",
                "id": "LoggingEmailAddress"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter your Password",
                "class": "form-input",
                "id": "loggingPassword"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm your Password",
                "class": "form-input",
                "id": "loggingPassword"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
