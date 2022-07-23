from django.shortcuts import render
import requests

def main(request):
    return render(request,'main.html')