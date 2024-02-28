from django.db import models
from club.models import Club
from django.contrib.auth import get_user_model

User = get_user_model()


class ClubInteraction(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following_user')
    club_id = models.ForeignKey(
        Club, on_delete=models.CASCADE, related_name='follow_club')

    class Meta:
        constraints = [
            models.constraints.UniqueConstraint(
                fields=['user', 'club_id'],
                name='unique_user_to_club'
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
