from rest_framework.views import APIView
from .serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from user import serializers


User = get_user_model()


class UserCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        data = request.data

        email = data.get('email', None)
        username = data.get('username', None)
        first_name = data.get('first_name', None)
        last_name = data.get('last_name', None)
        password = data.get('password', None)
        re_password = data.get('re_password', None)

        if not re_password:
            return Response({'detail': 'Confirmation password not set'}, status=status.HTTP_400_BAD_REQUEST)

        if password != re_password:
            return Response({'detail': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserCreateSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response({'success': 'User created successfully'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUpdateView(APIView):
    def put(self, request, format=None):
        data = request.data
        user = request.user
        try:
            user = User.objects.get(username=user.username)
        except User.DoesNotExist:
            return Response({'detail': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserCreateSerializer(user, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'User updated successfully'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, format=None):
        data = request.data
        user = request.user
        try:
            user = User.objects.get(user=user)
        except User.DoesNotExist:
            return Response({'detail': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserCreateSerializer(user, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'User updated successfully'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
