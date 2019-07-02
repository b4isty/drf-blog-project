from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.response import Response

from .serializers import PostSerializer, BlogImageSerializer
from .models import Post
from .parsers import MultipartFormencodeParser
from .permissions import IsOwnerOrReadonly

class PostCreateView(ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    parser_classes = [MultiPartParser, FormParser]
    queryset = Post.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print("$$$$$$$$$$$$$$$$$$$", request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data
        print("Serializer data&&&&&&&&&&&&&&&&&", data)
        return Response(data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadonly]
    queryset = Post.objects.all()

