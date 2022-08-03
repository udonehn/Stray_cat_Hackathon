from django.db import models

#데이터베이스 Table 만드는 코드
class Blog(models.Model):
    name = models.CharField(max_length = 100) #이름
    date = models.DateTimeField(auto_now_add=True) #등록일
    info2 = models.CharField(max_length = 100)
    info3 = models.CharField(max_length = 100)
    info4 = models.CharField(max_length = 100)      
    #latitude = models.TextField(max_length = 100)
    #longitude = models.TextField(max_length = 100)
    #어드민 창에서 데이터 name 필드를 이름으로 쓰는 코드
    def __str__(self):
        return self.name
    
    #미완성, 많은 부분에서 수정 필요