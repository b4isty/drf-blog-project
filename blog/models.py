from django.conf import settings
from django.db import models

from .utils import get_uploaded_file_name


class BlogImage(models.Model):
    image = models.ImageField(upload_to=get_uploaded_file_name)

    def __str__(self):
        return str(self.image)


class Post(models.Model):
    """
    This model Contains Post and related column
    """

    author = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    blog_image = models.ManyToManyField(BlogImage, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.user.email
