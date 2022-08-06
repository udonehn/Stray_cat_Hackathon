import imp
from django.shortcuts import render, redirect
from .models import Cat
from django.utils import timezone

def map2(request): #이거 이름 좀 잘 바꾸기 create 같은 거로
    if(request.method == 'POST'):
        post = Cat()
        post.name = request.POST['name']
        post.date = timezone.now()
        post.info2 = request.POST['info2']
        post.info3 = request.POST['info3']
        post.info4 = request.POST['info4']
        post.latitude = request.POST['latitude']
        post.longitude = request.POST['longitude']
        post.save()
        return redirect('main')
    return render(request,'cat_inf/map2.html')