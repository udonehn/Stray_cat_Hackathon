import imp
from django.shortcuts import render, redirect
from .models import Cat
from django.utils import timezone
from cat_inf.models import Cat
from django.http import HttpResponse
from django.core import serializers

def create(request): #이거 이름 좀 잘 바꾸기 create 같은 거로
    if(request.method == 'POST' or request.method =='FILES'):
        post = Cat()
        post.name = request.POST['name']
        post.date = timezone.now()
        post.species = request.POST['species']
        post.sex = request.POST['sex']
        post.neutral = request.POST['neutral']
        post.alert = request.POST['alert']
        post.character = request.POST['character']
        post.latitude = request.POST['latitude']
        post.longitude = request.POST['longitude']
        post.photo = request.FILES['photo']
        post.author = request.user
        post.save()
    return render(request,'cat_inf/create.html')

def getApi(request):
    cats = Cat.objects.all()
    cats_list = serializers.serialize('json', cats)
    return HttpResponse(cats_list, content_type="text/json-comment-filtered")