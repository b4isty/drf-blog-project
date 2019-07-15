from django.urls import path

from .views import FriendRequestView, FriendRequestAcceptIgnoreView

app_name = 'profiles'

urlpatterns = [
    path('friend-request/<int:pk>/', FriendRequestView.as_view(), name='friend_request'),
    path('friend-requests/', FriendRequestView.as_view(), name='friend_request'),
    path('friend-request/accept/<int:pk>/', FriendRequestAcceptIgnoreView.as_view(), name='accept_request'),
]