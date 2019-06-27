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

    # def create(self, request, *args, **kwargs):
    #     print(request.data)
    #     serializer = self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
        # serializer.save()
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        # user = CustomUser.objects.create_user(email=email, password=password)
        # return Response({"user": user.email}, status=status.HTTP_201_CREATED)

        # print("**", serializer.data)

        # first_name = serializer.data.get('first_name')
        # last_name = serializer.data.get('last_name')
        # username = serializer.data.get('username')
        # print("********************************************************")
        #

        # print("user", user)
        # user.first_name = first_name
        # user.last_name = last_name
        # return Response({"user": serializer.errors}, status=status.HTTP_201_CREATED)

    #
    # def create(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
