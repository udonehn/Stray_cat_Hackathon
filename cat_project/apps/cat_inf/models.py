from django.db import models

#데이터베이스 Table 만드는 코드
class Cat(models.Model):
    name = models.CharField(max_length = 100) #이름
    date = models.DateTimeField(auto_now_add=True) #등록일
    info2 = models.CharField(max_length = 100)
    info3 = models.CharField(max_length = 100)
    info4 = models.CharField(max_length = 100)      
    latitude = models.DecimalField(max_digits = 17, decimal_places = 13)
    longitude = models.DecimalField(max_digits = 17, decimal_places = 13)
    #어드민 창에서 데이터 name 필드를 이름으로 쓰는 코드
    def __str__(self):
        return self.name
    
    #미완성, 사진 업로드 구현 필요