from rest_framework import serializers
from .models import ClubBlogComment, UserBlogComment, CommentClubBlogComment, CommentUserBlogComment
from user.serializers import UserSerializer


class ClubBlogCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = ClubBlogComment
        fields = '__all__'


class UserBlogCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserBlogComment
        fields = '__all__'


class CommentClubBlogCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = CommentClubBlogComment
        fields = '__all__'


class CommentUserBlogCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = CommentUserBlogComment
        fields = '__all__'
