from django.urls import path
from .views import PostCreateView, PostDetailUpdateDestroyView

app_name = 'blog'

urlpatterns = [
    path('posts/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/', PostDetailUpdateDestroyView.as_view(), name='post_detail')
]
