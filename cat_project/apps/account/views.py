from asyncio.windows_events import NULL
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth import authenticate
from account.models import User,Bookmark
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages
from cat_inf.models import Cat, Complaint, Feed, Snack, injury
import json
from collections import Counter

"""
name = models.CharField(max_length = 100) #이름
    date = models.DateTimeField(auto_now_add=True) #등록일
    species = models.CharField(max_length = 100) #종 이름
    sex = models.IntegerField() #성별 / 1:암, 2:수, 3모름
    neutral = models.IntegerField() #중성화 여부 / 1:유 2:무, 3:모름
    alert = models.IntegerField() #사람 경계도 / 1:상, 2:중, 3:하
    character = models.CharField(max_length = 100) #특징
    latitude = models.DecimalField(max_digits = 17, decimal_places = 13)
    longitude = models.DecimalField(max_digits = 17, decimal_places = 13)
    photo = models.ImageField(blank=True, null=True, upload_to='cat_photo')
    author = models.ForeignKey(User, on_delete=models.CASCADE ,null=True)
    id = models.AutoField(primary_key=True)
"""


def main(request):
    cats = Cat.objects.all()
    cat_object_list = Cat.objects.all()
    user_id = request.user

    cat_list = []
    
    for cat in cat_object_list:
        is_marked = Bookmark.objects.filter(cat_id = cat.id , user_id = user_id).exists()
        cat_list.append(dict(name=cat.name,
                                date = cat.date,
                                species = cat.species,
                                sex = cat.sex,
                                neutral = cat.neutral,
                                alert = cat.alert,
                                character = cat.character,
                                latitude = cat.latitude,
                                longitude = cat.longitude,
                                photo = cat.photo,
                                author = cat.author,
                                id = cat.id,
                                is_marked=is_marked
                            ))
    content=dict(cats=cats, cat_list=cat_list)
    return render(request,'account/main.html',content)

def bookmark(request):
    if(request.method == 'POST'):
        is_marked = request.POST['is_marked']

        if(is_marked == 'false'):
            post = Bookmark()
            post.cat_id = request.POST['cat_id']
            post.user_id = request.user
            post.save()
            print("suc2(created)")
        else:
            id = int(request.POST['cat_id'])
            user_id = request.user
            print(user_id)
            Bookmark.objects.filter(cat_id = id , user_id = user_id).delete()
            print("suc1(deleted)")
            print(type(id))
    return render(request,'account/main.html')

def login(request):
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            messages.error(request,'사용자 ID 또는 비밀번호가 일치하지 않습니다.')
            return render(request, 'account/login.html')
        '''
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
        return redirect('main')
        #return render(request,'account/login.html')
        '''
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
                                            name=request.POST['name'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],)
            auth.login(request, user)
            return redirect('/')
        return render(request, 'account/signup.html')
    return render(request, 'account/signup.html')

def detail(request, cat_id):
    cat_detail = get_object_or_404(Cat, pk=cat_id)
    complaint_list = Complaint.objects.filter(cat_id=cat_id)
    last_feed_data = Feed.objects.filter(cat_id=cat_id).last()
    last_Snack_data = Snack.objects.filter(cat_id=cat_id).last()
    injury_list = injury.objects.filter(cat_id=cat_id)

    content = dict(
        cat_detail=cat_detail, 
        complaint_list=complaint_list,
        last_feed_data=last_feed_data,
        last_Snack_data=last_Snack_data,
        injury_list=injury_list,

        )
    return render(request, 'account/detail.html',content)

def mypage(request):
    user_id = request.user

    booked_id_list = list(Bookmark.objects.filter(user_id = user_id).values_list('cat_id',flat=True))
    my_cat_id_list = list(Cat.objects.filter(author = user_id).values_list('id',flat=True))

    complaint_find_list = list(set(booked_id_list + my_cat_id_list))
    complaint_list = Complaint.objects.filter(cat_id__in = complaint_find_list)
    
    injury_find_list = list(set(booked_id_list + my_cat_id_list))
    injury_list = injury.objects.filter(cat_id__in = injury_find_list)

    
    my_cat_list = Cat.objects.filter(id__in=my_cat_id_list)
    booked_cat_list = Cat.objects.filter(id__in=booked_id_list)
    content = dict(
        my_cat_list=my_cat_list, 
        booked_cat_list=booked_cat_list
        )

    return render(request,'account/mypage.html', content) 

def url_test(request):
    return render(request,'account/url_test.html') 