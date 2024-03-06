from pyexpat import model
from rest_framework import serializers
from .models import Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"


class UserInterestSerializer(serializers.RelatedField):
    def to_representation(self, value):
        return value.topic_name
