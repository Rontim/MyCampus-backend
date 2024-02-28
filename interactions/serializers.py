from rest_framework import serializers
from .models import ClubInteraction, User, UserInteraction


class ClubInteractionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClubInteraction
        fields = '__all__'

    def validate(self, attrs):
        user = attrs.get('user')
        club = attrs.get('club')

        if ClubInteraction.objects.filter(user=user, club_id=club).exists():
            raise serializers.ValidationError(
                'You are already following this club')

        return attrs


class UserInteractionSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInteraction
        fields = '__all__'

    def validate(self, attrs):
        user = attrs.get('user')
        following = attrs.get('follow_user')

        if UserInteraction.objects.filter(user=user, follow_user=following).exists():
            raise serializers.ValidationError(
                'You are already following this user')

        return attrs
