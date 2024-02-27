from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from topic import serializers
from .models import Topic
from django.http import Http404

class TopicView (APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get (self, request, slug):
        try:
            topic=Topic.objects.get(slug=slug)
        except Topic.DoesNotExist:
            raise Http404
        
        serializer=serializers.TopicSerializer(topic)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    
class TopicList (APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get (self, request):
        topics=Topic.objects.all()
        serializer=serializers.TopicSerializer(topics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)