from os import read
from rest_framework import serializers
from interactions.models import ClubInteraction, UserInteraction
from django.contrib.auth import get_user_model

from topic.serializers import UserInterestSerializer

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()
    clubs = serializers.SerializerMethodField()
    interest = UserInterestSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', "email", 'first_name',
                  'last_name', 'followers', 'following', 'clubs', 'interest')

    def get_followers(self, obj):
        return UserInteraction.objects.filter(follow_user=obj).count()

    def get_following(self, obj):
        return UserInteraction.objects.filter(user=obj).count()

    def get_clubs(self, obj):
        return ClubInteraction.objects.filter(user=obj).count()


class MentionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
        read_only_fields = ['username']
