from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from club import serializers
from .models import Club
from django.http import Http404

class ClubView (APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get (self, request, slug):
        try:
            club=Club.objects.get(slug=slug)
        except Club.DoesNotExist:
            raise Http404
        
        serializer=serializers.ClubSerializer(club)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    
class ClubList (APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get (self, request):
        clubs=Club.objects.all()
        serializer=serializers.ClubSerializer(clubs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)