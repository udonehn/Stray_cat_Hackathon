from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from cat_inf.models import Cat
from django.http import HttpResponse
from django.core import serializers

def getApi(request):
    cats = Cat.objects.all()
    cats_list = serializers.serialize('json', cats)
    return HttpResponse(cats_list, content_type="text/json-comment-filtered")

def apiTest(request):
    return render(request, 'account/apiTest.html')

def main(request):
    cats = Cat.objects.all()
    count = Cat.objects.count()
    content = {
        "cats":cats,
        "count":count
    }
    return render(request,'account/main.html',content)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
        return redirect('main')
        #return render(request,'account/login.html')
    else:
        form = AuthenticationForm()
        return render(request,'account/login.html', {'form':form})

def logout(request):
    auth_logout(request)
    return redirect('main')

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