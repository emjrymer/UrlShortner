from django.contrib import admin

# Register your models here.
from app.models import Click, Bookmark

admin.site.register(Bookmark),
admin.site.register(Click)
