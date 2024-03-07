from ast import List
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound

from topic.serializers import TopicSerializer


from .models import UserBlog, ClubBlog
from .serializers import ClubBlogsSerializer, UserBlogSerializer, ClubBlogSerializer, UserBlogsSerializer

from club.models import Club
from topic.models import Topic
from django.contrib.auth import get_user_model

User = get_user_model()


class CreateBlog(APIView):

    def get_club(self, slug):
        try:
            club = Club.objects.get(slug=slug)
        except Club.DoesNotExist:
            raise NotFound
        return club

    def get_topics(self, topics):
        blog_topics = []
        for topic in topics:
            topic = TopicSerializer(data=topic)
            blog_topics.append(topic)

        return blog_topics

    def post(self, request):
        data = request.data
        data['author'] = request.user.pk

        serializer = UserBlogSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReadBlog(APIView):

    def get_user_blog(self, slug):
        try:
            blog = UserBlog(slug=slug)
        except UserBlog.DoesNotExist:
            return None
        return blog

    def get_club_blog(self, slug):
        try:
            blog = ClubBlog.objects.get(slug=slug)
        except ClubBlog.DoesNotExist:
            return None
        return blog

    def get(self, request, slug):

        club_blog, user_blog = self.get_user_blog(
            slug=slug), self.get_club_blog(slug=slug)

        if club_blog:
            serializer = ClubBlogSerializer(data=club_blog)
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if user_blog:
            serializer = UserBlogSerializer(data=user_blog)
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class BlogsListView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        club_blogs = ClubBlog.objects.all()
        user_blugs = UserBlog.objects.all()

        clubblogs_serializer = ClubBlogsSerializer(
            instance=club_blogs, many=True)
        userblogs_serializer = UserBlogsSerializer(
            instance=user_blugs, many=True)

        response = userblogs_serializer.data + clubblogs_serializer.data
        return Response(response)
