from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

def main(request):
    return render(request,'C:/vscode/STRAY CAT/cat_project/templates/main.html')