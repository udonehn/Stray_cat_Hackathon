from django.db import models
from django.contrib.auth.models import User

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
    #어드민 창에서 데이터 name 필드를 이름으로 쓰는 코드
    def __str__(self):
        return self.name