from rest_framework import serializers
from .models import Club


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ('club_name', 'slug', 'description')


class ClubDetailSerializer(serializers.ModelSerializer):
    pass
