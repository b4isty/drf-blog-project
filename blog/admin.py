from django.contrib import admin

from .models import Post, BlogImage, Comment, Like

admin.site.register([Post, BlogImage, Comment, Like])
