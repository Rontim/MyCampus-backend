from os import read
from wsgiref.validate import validator
from rest_framework import serializers
from .models import BlogComment, ReplyComment
from user.serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = ['unique_id', 'comment', 'commentor',
                  'blog', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class ReplySerializer(serializers.ModelSerializer):

    class Meta:
        model = ReplyComment
        fields = '__all__'


class RepliesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplyComment
        fields = ['reply', 'replier', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class CommentListSerializer(serializers.ModelSerializer):
    replies = RepliesSerializer(many=True, read_only=True)

    class Meta:
        model = BlogComment
        fields = ['unique_id', 'comment', 'commentor',
                  'replies', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
