import json
from rest_framework import serializers

from topic.models import Topic
from .models import UserBlog, ClubBlog
from topic.serializers import TopicSerializer, UserInterestSerializer


class UserBlogSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True)

    def to_internal_value(self, data):
        if 'content' in data:
            data['content'] = json.dumps(data['content'])

        return super().to_internal_value(data)

    def to_representation(self, instance):
        representaion = super().to_representation(instance)
        if 'content' in representaion:
            representaion['content'] = json.loads(representaion['content'])

        return representaion

    def create(self, validated_data):
        topics = validated_data.pop('topics')
        blog = UserBlog.objects.create(**validated_data)
        for topic in topics:
            topic, _ = Topic.objects.get_or_create(
                topic_name=topic["topic_name"])

            blog.topics.add(topic.pk)  # type: ignore
        return blog

    class Meta:
        model = UserBlog
        fields = ['id', 'title', 'slug', 'thumbnail',
                  'content', 'topics', 'updated_at', 'created_at', 'author', 'author_type']
        read_only_fields = ['id', 'updated_at', 'created_at', 'author_type']


class ClubBlogSerializer(serializers.ModelSerializer):

    def to_internal_value(self, data):
        if 'content' in data:
            data['content'] = json.dumps(data['content'])

        return super().to_internal_value(data)

    def to_representation(self, instance):
        representaion = super().to_representation(instance)
        if 'content' in representaion:
            representaion['content'] = json.loads(representaion['content'])

        return representaion

    class Meta:
        model = ClubBlog
        fields = ['id', 'title', 'slug', 'thumbnail',
                  'content', 'topics', 'updated_at', 'created_at', 'author_type']
        read_only_fields = ['id', 'updated_at', 'created_at', 'author_type']


class ClubBlogsSerializer(serializers.ModelSerializer):
    topics = UserInterestSerializer(many=True, read_only=True)

    class Meta:
        model = ClubBlog
        fields = ['title', 'slug', 'thumbnail', 'topics', 'author_type']


class UserBlogsSerializer(serializers.ModelSerializer):
    topics = UserInterestSerializer(many=True, read_only=True)

    class Meta:
        model = UserBlog
        fields = ['title', 'slug', 'thumbnail', 'topics', 'author_type']
