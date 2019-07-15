from django.contrib import admin

# Register your models here.

from .models import FriendRequest, Profile


admin.site.register([FriendRequest, Profile])


