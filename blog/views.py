from ast import List
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound

from topic.serializers import TopicSerializer


from .models import Blog
from .serializers import BlogCreateRetrieveSerializer, BlogListingSerializer

from club.models import Club
from topic.models import Topic
from django.contrib.auth import get_user_model

User = get_user_model()


class CreateBlog(APIView):

    def get_user(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound
        return user

    def get_club(self, slug):
        try:
            club = Club.objects.get(slug=slug)
        except Club.DoesNotExist:
            raise NotFound

        return club

    def post(self, request):
        author_type = request.data.get('author_type')
        title = request.data.get('title')
        content = request.data.get('content')
        thumbnail = request.data.get('thumbnail')
        topics = request.data.get('topics')
        author = request.data.get('author')

        data = {
            'title': title,
            'author_type': author_type,
            'content': content,
            'thumbnail': thumbnail,
            'topics': topics
        }

        if author_type == 'user':
            author = self.get_user(username=author)
            data['author_user'] = author.get_username()
        if author_type == 'club':
            data['author_club'] = self.get_club(slug=author).slug

        print(data)

        serializer = BlogCreateRetrieveSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReadBlog(APIView):

    def get_blog(self, slug):
        try:
            blog = Blog.objects.get(slug=slug)
        except Blog.DoesNotExist:
            raise NotFound
        return blog

    def get(self, request, slug):
        blog = self.get_blog(slug=slug)
        serializer = BlogCreateRetrieveSerializer(instance=blog)
        return Response(serializer.data)


class BlogsListView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogListingSerializer(blogs, many=True)
        return Response(serializer.data)
