from django.contrib import admin
from .models import Blog

#어드민 사이트에 Blog 테이블을 띄워주는 코드
admin.site.register(Blog) 

#admin사이트 아이디:admin, 패스워드:1234