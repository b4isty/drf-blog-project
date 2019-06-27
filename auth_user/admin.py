from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationFor, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationFor
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ['email', ]


admin.site.register(CustomUser, CustomUserAdmin)
