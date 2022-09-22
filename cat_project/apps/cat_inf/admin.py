from django.contrib import admin
from .models import Cat, Complaint, Feed, Snack, Injury

admin.site.register(Cat)
admin.site.register(Complaint)
admin.site.register(Feed)
admin.site.register(Snack)
admin.site.register(Injury)