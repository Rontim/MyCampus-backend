from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from blog.views import User
from topic.models import Topic
from topic.serializers import TopicSerializer
from user.serializers import UserSerializer


class AddUserInterests(APIView):
    def get_topic(self, topic):
        return Topic.objects.get_or_create(topic_name=topic)

    def post(self, request, *args, **kwargs):
        user = request.user
        topics = request.data.get('topics')
        for topic in topics:
            topic = self.get_topic(topic)
            user.interest.add(topic[0].pk)
        user.save()
        serializer = UserSerializer(instance=user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetSUserProfile(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_user(self, username):
        try:
            user = User.objects.get(username=username)

        except User.DoesNotExist:
            raise NotFound

        return user

    def get(self, request, username):
        profile = self.get_user(username)

        serializer = UserSerializer(instance=profile)

        return Response(serializer.data, status=status.HTTP_200_OK)
