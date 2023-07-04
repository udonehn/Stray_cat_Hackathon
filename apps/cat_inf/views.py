from calendar import isleap
import imp
import json
from urllib import request
from django.shortcuts import render, redirect
from django.utils import timezone
from cat_inf.models import Cat, Complaint, Feed, Snack, Injury
from account.models import User,Bookmark
from django.http import HttpResponse
from django.core import serializers
import datetime as dt

def post(self, request):
    cats_id = request.data.get('cats_id', None)
    favorite_text = request.data.get('favorite_text', True)

    if favorite_text == 'favorite_border':
        is_liked = True
    else:
        is_liked = False
    request.session.session_key

def create(request):
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
        post.photo = mask_circle_transparent(request.FILES['photo'])
        post.author = request.user
        post.save()
    return render(request,'cat_inf/create.html')



def getApi(request):
    cats = Cat.objects.all()
    cats_list = serializers.serialize('json', cats)
    return HttpResponse(cats_list, content_type="text/json-comment-filtered")

def getApi_marked(request):
    cat_object_list = Cat.objects.all()
    user_id = request.user

    cat_list = []
    
    for cat in cat_object_list:
        is_marked = Bookmark.objects.filter(cat_id = cat.id , user_id = user_id).exists()
        cat_list.append(dict(name=cat.name,
                                is_marked=is_marked
                            ))
    result = json.dumps({'list':cat_list})
    return HttpResponse(result, content_type="text/json-comment-filtered")

def complaint(request):
    if(request.method == 'POST'):
        form_tag = int(request.POST['form_tag'])

        if form_tag == 0:
            post = Complaint()
            cat_id = int(request.POST['cat_id'])
            post.cat_id = cat_id

            post.form_tag = request.POST['form_tag']
            post.date = timezone.now()
            post.complaint_kind = request.POST['complaint_kind']
            post.character = request.POST['character']
            post.author = request.user
            post.save()

            cat = Cat.objects.filter(id = cat_id).first()
            cat.complaint_count = int(cat.complaint_count)+1
            cat.save()
        elif form_tag == 1:
            x = float(request.POST['latitude'])
            y = float(request.POST['longitude'])
            cat_object_list = list(Cat.objects.all())
            for cat in cat_object_list:
                x2 = float(cat.latitude)
                y2 = float(cat.longitude)
                distance = ((x-x2)**2 + (y-y2)**2)**0.5
                if distance < 0.0015:
                    post = Complaint()
                    cat_id = cat.id
                    post.cat_id = cat_id
                    post.latitude = x
                    post.longitude = y

                    post.form_tag = request.POST['form_tag']
                    post.date = timezone.now()
                    post.complaint_kind = request.POST['complaint_kind']
                    post.character = request.POST['character']
                    post.author = request.user
                    post.save()

                    cat = Cat.objects.filter(id = cat_id).first()
                    cat.complaint_count = int(cat.complaint_count)+1
                    cat.save()

        return render(request,'account/main.html')
    else:
        default_cat_id = request.GET.get('cat_id', None)
        content = dict(default_cat_id=default_cat_id)
        return render(request,'cat_inf/complaint.html', content)

def injury(request):
    if(request.method == 'POST'):
        post = Injury()
        cat_id = int(request.POST['cat_id'])
        post.cat_id = cat_id

        post.date = timezone.now()
        post.injury_kind = request.POST['injury_kind']
        post.character = request.POST['character']
        post.author = request.user
        post.save()

        cat = Cat.objects.filter(id = cat_id).first()
        cat.injury_count = int(cat.injury_count)+1
        cat.save()

        return render(request,'account/main.html')
    else:
        default_cat_id = request.GET.get('cat_id', None)
        content = dict(default_cat_id=default_cat_id)
        return render(request,'cat_inf/injury.html', content)

def feed(request):
    if(request.method == 'POST'):
        post = Feed()
        cat_id = int(float(request.POST['cat_id']))
        post.cat_id = cat_id
        post.date = timezone.now()
        post.author = request.user
        post.save()

        last_feed_data = Feed.objects.filter(cat_id=cat_id).last()
        date = last_feed_data.date

        ampm = date.strftime('%p')
        ampm_kr = '오전' if ampm == 'AM' else '오후'
        hour = (date.hour) if ampm == 'AM' else (date.hour-12)

        data = f'{date.year}년 {date.month}월 {date.day}일 {hour}:{date.minute} {ampm_kr}'
    return HttpResponse(data)

def snack(request):
    if(request.method == 'POST'):
        post = Snack()
        cat_id = int(float(request.POST['cat_id']))
        post.cat_id = cat_id
        print(int(request.POST['cat_id']))
        post.date = timezone.now()
        post.author = request.user
        post.save()

        last_snack_data = Snack.objects.filter(cat_id=cat_id).last()
        date = last_snack_data.date

        ampm = date.strftime('%p')
        ampm_kr = '오전' if ampm == 'AM' else '오후'
        hour = (date.hour) if ampm == 'AM' else (date.hour-12)

        data = f'{date.year}년 {date.month}월 {date.day}일 {hour}:{date.minute} {ampm_kr}'
    return HttpResponse(data)


#여기부터는 코드에 사용되는 함수

def rescale(self, data, width, height, force=True):
    from io import BytesIO
    from PIL import Image

    max_width = width
    max_height = height

    input_file = BytesIO(data.read())
    img = Image.open(input_file)
    if not force:
        img.thumbnail((max_width, max_height), Image.ANTIALIAS)
    else:
        src_width, src_height = img.size
        src_ratio = float(src_width) / float(src_height)
        dst_width, dst_height = max_width, max_height
        dst_ratio = float(dst_width) / float(dst_height)

        if dst_ratio < src_ratio:
            crop_height = src_height
            crop_width = crop_height * dst_ratio
            x_offset = int(src_width - crop_width) // 2
            y_offset = 0
        else:
            crop_width = src_width
            crop_height = crop_width / dst_ratio
            x_offset = 0
            y_offset = int(src_height - crop_height) // 3
        img = img.crop((x_offset, y_offset, x_offset+int(crop_width), y_offset+int(crop_height)))
        img = img.resize((dst_width, dst_height), Image.ANTIALIAS)

    image_file = BytesIO()
    img.save(image_file, 'JPEG')
    data.file = image_file
    return data

def mask_circle_transparent(data, offset=0):
    from PIL import Image, ImageDraw
    from io import BytesIO

    input_file = BytesIO(data.read())
    img = Image.open(input_file)
    offset = offset
    #동그라미 필터 생성
    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((offset, offset, img.size[0] - offset, img.size[1] - offset), fill=255)

    #필터 적용
    result = img.putalpha(mask)

    #파일 변환 시킨스
    image_file = BytesIO()
    img.save(image_file, 'PNG')
    data.file = image_file
    return data