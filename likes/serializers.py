from rest_framework import serializers
from .models import BlogLike


class BlogLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogLike
        fields = ['blog', 'user', 'like_time']
        read_only_fields = ['like_time']
