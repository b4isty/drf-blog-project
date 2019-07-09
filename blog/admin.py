from django.contrib import admin

from .models import Post, BlogImage, Comment

admin.site.register([Post, BlogImage, Comment])
