from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

def main(request):
    return render(request,'account/main.html')

def login(request):
    if request.method == 'POST':
        return render(request,'account/login.html')
    else:
        return render(request,'account/login.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                                            username=request.POST['username'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],)
            auth.login(request, user)
            return redirect('/')
        return render(request, 'account/signup.html')
    return render(request, 'account/signup.html')