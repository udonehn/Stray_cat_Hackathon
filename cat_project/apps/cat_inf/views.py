from django.shortcuts import render, redirect
from .models import Blog
def map2(request):
    return render(request,'cat_inf/map2.html')

def create(request):
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')