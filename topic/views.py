from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from blog.models import Blog
from topic import serializers
from .models import Topic
from django.http import Http404


class TopicView (APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, slug):
        try:
            topic = Topic.objects.get(slug=slug)
        except Topic.DoesNotExist:
            raise Http404

        serializer = serializers.TopicSerializer(topic)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TopicList (APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        topics = Topic.objects.all()
        serializer = serializers.TopicSerializer(topics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TrendingTopics(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        # I want to get the topics that have been used on blogs the most in the last 7 days
        # I will get the blogs that have been created in the last 7 days
        # Then I will get the topics of these blogs
        # Then I will count the topics
        # Then I will return the top 10 topics
        today = datetime.now() + timedelta(hours=5)
        last_week = today - timedelta(days=7)
        blogs = Blog.objects.filter(
            created_at__range=[last_week, today])
        topics = {}

        for blog in blogs:
            for topic in blog.topics.all():
                if topic in topics:
                    topics[topic] += 1
                else:
                    topics[topic] = 1

        sorted_topics = sorted(
            topics, key=topics.get, reverse=True)[:10]  # type: ignore
        serializer = serializers.TopicSerializer(sorted_topics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
