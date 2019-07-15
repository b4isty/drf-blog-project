from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.response import Response

from .serializers import PostSerializer, BlogImageSerializer, CommentsSerializer, PostDetailSerializer, LikeSerializer
from .models import Post, Comment, Like
from .parsers import MultipartFormencodeParser
from .permissions import IsAuthorOrReadonly, IsUserOrReadOnly


class PostCreateView(ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    parser_classes = [MultiPartParser, FormParser]
    queryset = Post.objects.all()

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data
        return Response(data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailSerializer
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


class LikeCreateView(ListCreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsUserOrReadOnly]
    queryset = Like.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.validated_data:
            serializer.validated_data['user'] = request.user
            print(serializer.data)
            obj, created = Like.objects.get_or_create(**serializer.validated_data)
            if not created:
                obj.delete()
                return Response([])
        return Response(serializer.data, status=status.HTTP_201_CREATED)



    # def perform_create(self, serializer):
    #     print("***********", serializer.data)
    #     serializer.save(user=self.request.user)





# class PostCommentDetailView(RetrieveAPIView):
#     serializer_class = PostCommentSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly, IsUserOrReadOnly, IsAuthorOrReadonly]
#     queryset = Comment.objects.all()

# class PostDetailView

