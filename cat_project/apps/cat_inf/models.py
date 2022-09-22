from django.db import models
from account.models import User

#데이터베이스 Table 만드는 코드
class Cat(models.Model):
    name = models.CharField(max_length = 100) #이름
    date = models.DateTimeField(auto_now_add=True) #등록일
    species = models.CharField(max_length = 100) #종 이름
    sex = models.CharField(max_length = 100) #성별
    neutral = models.CharField(max_length = 100) #중성화 여부
    alert = models.CharField(max_length = 100) #사람 경계도
    character = models.CharField(max_length = 100) #특징
    latitude = models.DecimalField(max_digits = 17, decimal_places = 13)
    longitude = models.DecimalField(max_digits = 17, decimal_places = 13)
    photo = models.ImageField(blank=True, null=True, upload_to='cat_photo')
    author = models.ForeignKey(User, on_delete=models.CASCADE ,null=True)
    id = models.AutoField(primary_key=True)
    complaint_count = models.IntegerField(default=0) #민원 횟수
    #어드민 창에서 데이터 name 필드를 이름으로 쓰는 코드
    def __str__(self):
        return self.name

class Complaint(models.Model):
    form_tag = models.IntegerField() # 0: 고양이를 앎, 1:지역
    #1인 경우, 추가 데이터
    latitude = models.DecimalField(max_digits = 17, decimal_places = 13, null=True)
    longitude = models.DecimalField(max_digits = 17, decimal_places = 13, null=True)
    #공통 데이터
    cat_id = models.IntegerField(null=True) #고양이 등록 id
    date = models.DateTimeField(auto_now_add=True) #등록일
    complaint_kind = models.TextField(blank=False) #민원 체크박스 읽어옴
    character = models.TextField(null=True) #특징(기타 사항)
    author = models.EmailField()

class Feed(models.Model):
    cat_id = models.IntegerField(null=True)
    author = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    
class Snack(models.Model):
    cat_id = models.IntegerField(null=True)
    author = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)
