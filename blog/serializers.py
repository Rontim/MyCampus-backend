import json
from rest_framework import serializers

from topic.models import Topic
from .models import Blog
from topic.serializers import TopicSerializer, UserInterestSerializer


class BlogCreateRetrieveSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True)

    def to_internal_value(self, data):
        if 'content' in data:
            data['content'] = json.dumps(data['content'])
        return super().to_internal_value(data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if 'content' in representation:
            representation['content'] = json.loads(representation['content'])

        return representation

    def create(self, validated_data):
        print(validated_data)

        topics_data = validated_data.pop('topics', [])

        blog = Blog.objects.create(**validated_data)

        for topic_data in topics_data:
            topic, _ = Topic.objects.get_or_create(
                topic_name=topic_data["topic_name"])
            blog.topics.add(topic)
        return blog

    class Meta:
        model = Blog
        fields = ['id', 'title', 'slug', 'author_type', 'author_user', 'author_club', 'thumbnail', 'content',
                  'topics', 'updated_at', 'created_at']
        read_only_fields = ['id', 'updated_at', 'created_at']


class BlogListingSerializer(serializers.ModelSerializer):
    topics = UserInterestSerializer(many=True, read_only=True)
    author = serializers.SerializerMethodField()

    def to_representation(self, instance):
        return super().to_representation(instance)

    class Meta:
        model = Blog
        fields = ['title', 'slug', 'thumbnail',
                  'topics', 'author_type', 'author']

    def get_author(self, instance):
        print(instance)
        if instance.author_type == 'user':
            return instance.author_user.username
        return instance.author_club.club_name
