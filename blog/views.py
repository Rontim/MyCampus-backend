from ast import List
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics

from django.db.models import Q
from datetime import datetime, timedelta

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


class BlogsByAuthor(APIView):
    permission_classes = [permissions.AllowAny]

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

    def get(self, request, author_type, author):
        if author_type == 'user':
            author = self.get_user(username=author)
            blogs = Blog.objects.filter(author_user=author)
        if author_type == 'club':
            author = self.get_club(slug=author)
            blogs = Blog.objects.filter(author_club=author)

        serializer = BlogListingSerializer(blogs, many=True)
        return Response(serializer.data)


# Searching and filtering blogs

class SearchBlogs(APIView):
    '''
    Search and filter blogs based on the following parameters:
    - search
    - topic
    - author
    - period
    - title

    The search parameter is a string that is used to search for blogs based on the title, content, author, and topics.

    The topic parameter is a string that is used to filter blogs based on the topic.

    The author parameter is a string that is used to filter blogs based on the author.

    The period parameter is a string that is used to filter blogs based on the period. The period 
    can be one of the following values: today, this_week, this_month, this_year.

    The title parameter is a string that is used to filter blogs based on the title.

    '''

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        topic = request.GET.get('topic')
        author = request.GET.get('author')
        period = request.GET.get('period')
        title = request.GET.get('title')
        search = request.GET.get('q')

        queryset = Blog.objects.all()

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(content__icontains=search) | Q(topics__topic_name__icontains=search) | Q(author_user__username__icontains=search) | Q(author_club__slug__icontains=search))

        if title:
            queryset = queryset.filter(title__icontains=title)

        if topic:
            queryset = queryset.filter(topics__topic_name=topic)

        if author:
            queryset = queryset.filter(
                Q(author_user__username=author) | Q(author_club__slug=author))

        if period:
            if period == 'today':
                queryset = queryset.filter(
                    created_at__date=datetime.now().date)

            elif period == 'this_week':
                today = datetime.now().date()
                start_date = today - timedelta(days=today.weekday())
                end_date = start_date + timedelta(days=6)
                queryset = queryset.filter(
                    created_at__range=[start_date, end_date])
            elif period == 'this_month':
                current_month = datetime.now().month
                current_year = datetime.now().year
                queryset = queryset.filter(
                    created_at__month=current_month, created_at__year=current_year)

            elif period == 'this_year':
                current_year = datetime.now().year
                queryset = queryset.filter(created_at__year=current_year)

        serializer = BlogListingSerializer(queryset, many=True)
        return Response(serializer.data)


class TrendingBlogs(APIView):
    '''
    Get the trending blogs
    '''
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        blog = Blog.objects.all().order_by('-likes')[:20]

        serializer = BlogListingSerializer(blog, many=True)
        return Response(serializer.data)
