from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView
from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from .forms import CustomUserCreationForm, CustomUserAuthenticationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('product_list')
    else:
        form = CustomUserAuthenticationForm()
    return render(request, 'accounts/signin.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('signin')

def check_inactivity(request):
    if request.user.is_authenticated:
        last_login = request.user.last_login
        if last_login and timezone.now() - last_login > timedelta(days=60):
            logout(request)
            return redirect('signin')
    return redirect('product_list')
