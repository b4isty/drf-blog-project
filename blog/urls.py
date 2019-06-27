from django.urls import path
from .views import PostCreateView

app_name = 'blog'

urlpatterns = [
    path('posts/', PostCreateView.as_view(), name='post_create')
]
