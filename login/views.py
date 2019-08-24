from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import *

# Create your views here.
def homepage(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'homepage.html', {})

def register(request):   
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('loginHomepage')
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    return render(request, 'register.html', context={})

def logout_request(request):
    logout(request)
    return redirect('login')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('loginHomepage')

    return render(request, 'login.html', {})
