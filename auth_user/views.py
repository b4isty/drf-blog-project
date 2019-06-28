from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework import status

from .models import CustomUser
from .serializers import RegisterUserSerializer


class RegisterView(CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny, ]
    queryset = CustomUser.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
