from django.contrib import admin
from .models import HomePageData, Comment, Catagory, Post


# Register your models here.
admin.site.register(HomePageData)
admin.site.register(Comment)
admin.site.register(Catagory)
admin.site.register(Post)