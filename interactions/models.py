from django.db import models
from club.models import Club
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class ClubInteraction(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following_user')
    club_id = models.ForeignKey(
        Club, on_delete=models.CASCADE, related_name='follow_club')

    def validate_user_to_club(self, user, club):
        if ClubInteraction.objects.filter(user=user, club_id=club).exists():
            raise serializers.ValidationError(
                'You are already following this club')

    def validate(self, attrs):
        user = attrs.get('user')
        club = attrs.get('club')

        self.validate_user_to_club(user, club)

        return attrs

    class Meta:
        constraints = [
            models.constraints.UniqueConstraint(
                fields=['user', 'club_id'],
                name='unique_user_to_club',
                violation_error_message=('You are already following this club')
            )
        ]


class UserInteraction(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='current_user')
    follow_user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.constraints.UniqueConstraint(
                fields=['user', 'follow_user'],
                name='unique_user_to_user'
            )
        ]
