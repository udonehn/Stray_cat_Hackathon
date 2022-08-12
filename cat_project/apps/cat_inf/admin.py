from django.contrib import admin
from .models import Cat
from .models import Image

admin.site.register(Cat)
admin.site.register(Image)