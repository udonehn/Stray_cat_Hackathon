from django.db import models

#데이터베이스 Table 만드는 코드
class Cat(models.Model):
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
    #사용자 이름(ID)도 받아올 수 있어야 함

    #어드민 창에서 데이터 name 필드를 이름으로 쓰는 코드
    def __str__(self):
        return self.name

class Image(models.Model):
    file = models.ImageField(upload_to='cat_photo')
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)
