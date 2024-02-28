from rest_framework import serializers
from interactions.models import ClubInteraction, UserInteraction
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()
    clubs = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('username', "email", 'first_name',
                  'last_name', 'followers', 'following', 'clubs')

    def get_followers(self, obj):
        return UserInteraction.objects.filter(follow_user=obj).count()

    def get_following(self, obj):
        return UserInteraction.objects.filter(user=obj).count()

    def get_clubs(self, obj):
        return ClubInteraction.objects.filter(user=obj).count()
