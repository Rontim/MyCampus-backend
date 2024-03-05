from rest_framework import serializers
from .models import ClubBlogLike, UserBlogLike

class ClubBlogLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubBlogLike
        fields = "__all__"

class UserBlogLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBlogLike
        fields = "__all__"