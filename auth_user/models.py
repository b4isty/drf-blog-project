from django.db import models

from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=2, default='')
    email = models.EmailField(unique=True, max_length=50, null=True)
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []






