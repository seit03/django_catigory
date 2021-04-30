from django.contrib import admin

# Register your models here.

from category_user.models import Category, TVShow, Comment

admin.site.register(Category)
admin.site.register(TVShow)
admin.site.register(Comment)
