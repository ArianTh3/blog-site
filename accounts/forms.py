# accounts/forms.py

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

User = get_user_model()


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'class': 'input100',
            'placeholder': 'Email',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input100',
            'placeholder': 'Password',
        })
    )


class CustomCreateUserForm(UserCreationForm):
    email = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'johndoe@gmail.com'})
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email",)

from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={'class': 'input100', 'placeholder': 'Email'})
    )


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'New Password'})
    )
    new_password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Confirm New Password'})
    )