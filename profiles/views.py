from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, GenericAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin

from .models import FriendRequest, Profile
from .permissions import IsOwner
from .serializers import FriendRequestSerializer, AcceptIgnoreFriendRequestSerializer


User = get_user_model()


class FriendRequestView(ListCreateAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = FriendRequest.objects.all()

    # lookup_url_kwarg = ['accept_id']

    def create(self, request, *args, **kwargs):
        to_user = User.objects.get(id=kwargs['pk'])
        data = {"to_user": to_user.id}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        obj1 = FriendRequest.objects.filter(to_user=to_user, from_user=request.user)
        obj2 = FriendRequest.objects.filter(to_user=request.user, from_user=to_user)
        if obj1.exists():
            return Response({"message": "Friend request already sent "})
        elif obj2.exists():
            msg = f"{to_user.email} already sent you a friend request"
            return Response({"message": msg})
        else:
            obj, created = FriendRequest.objects.get_or_create(to_user=to_user, from_user=request.user)
            if not created:
                return Response({"message": "Friend request already sent "})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def get_queryset(self):
    #

    # def get_object(self):


class FriendRequestAcceptIgnoreView(CreateAPIView):
    serializer_class = AcceptIgnoreFriendRequestSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]
    queryset = Profile.objects.all()

    def post(self, request, *args, **kwargs):
        from_user = get_object_or_404(User, pk=kwargs['pk'])
        profile_obj = self.get_queryset().get(user=request.user)
        friend_req = FriendRequest.objects.filter(from_user=from_user.id, to_user=request.user)
        if friend_req.exists():
            friend_req_obj = friend_req.first()
            data = {"friends": [from_user.id]}
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            profile_obj.friends.add(from_user)
            requested_user = Profile.objects.get(user=from_user)
            requested_user.friends.add(request.user)
            friend_req_obj.delete()
            respns = {"message": "Friend request accepted", 'from_user': serializer.data}
            return Response(respns, status=status.HTTP_200_OK)
        return Response({"message": "Friend request doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
