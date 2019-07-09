from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.response import Response

from .serializers import PostSerializer, BlogImageSerializer, CommentsSerializer
from .models import Post, Comment
from .parsers import MultipartFormencodeParser
from .permissions import IsAuthorOrReadonly, IsUserOrReadOnly


class PostCreateView(ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    parser_classes = [MultiPartParser, FormParser]
    queryset = Post.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data
        return Response(data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadonly]
    queryset = Post.objects.all()


class CommentCreateAPI(ListCreateAPIView):
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDetailUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsUserOrReadOnly]
    queryset = Comment.objects.all()



