from django.db import models

#데이터베이스 Table 만드는 코드
class Blog(models.Model):
    title = models.CharField(max_length = 100)
    data = models.DateTimeField(auto_now_add=True)

    #어드민 창에서 데이터 title 필드를 이름으로 쓰는 코드
    def __str__(self):
        return self.title