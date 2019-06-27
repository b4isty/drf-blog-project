from django.db import models
from django.conf import settings

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
        return self.author
