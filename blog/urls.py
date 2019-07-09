from django.urls import path
from .views import PostCreateView, PostDetailUpdateDestroyView, CommentCreateAPI, CommentDetailUpdateDestroyAPI

app_name = 'blog'

urlpatterns = [
    path('posts/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/', PostDetailUpdateDestroyView.as_view(), name='post_detail'),
    path('comments/', CommentCreateAPI.as_view(), name='comment'),
    path('comments/<int:pk>/', CommentDetailUpdateDestroyAPI.as_view(), name='comment_detail'),

]
