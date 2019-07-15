from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

from blog.utils import get_uploaded_file_name


# Create your models here.


class FriendRequest(models.Model):
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                  related_name='friend_request_sender')
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                related_name='friend_request_receiver')

    # accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"sender {self.from_user.email}  receiver {self.to_user.email}"


# class Friendship(models.Model):
#     friends = models.ManyToManyField(settings.AUTH_USER_MODEL)
#     current_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owner', on_delete=models.CASCADE, null=True)
#
#     def __str__(self):
#         return str(self.current_user.email)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='friends')
    avatar = models.ImageField(upload_to=get_uploaded_file_name, blank=True, null=True)

    def __str__(self):
        return self.user.email


def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass


post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)
