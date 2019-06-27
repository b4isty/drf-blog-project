from django.contrib import admin

from .models import Post, BlogImage

admin.site.register([Post, BlogImage])