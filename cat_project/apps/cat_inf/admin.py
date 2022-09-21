from django.contrib import admin
from .models import Cat, Complaint, Feed

admin.site.register(Cat)
admin.site.register(Complaint)
admin.site.register(Feed)