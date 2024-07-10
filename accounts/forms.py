from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Iltimos, emailingizni kiriting'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Iltimos, familyangizni kiriting'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Parol kiriting'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Parolni tasdiqlang'}))

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username' ,'email', 'password1', 'password2')

class CustomUserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Iltimos, ismingizni kiriting'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Parol kiriting'}))
