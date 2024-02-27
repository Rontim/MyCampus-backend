from django.db import models
from django.contrib.auth import get_user_model
from club.models import Club

class Notifications(models.Model):
    content = models.TextField()
    create_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class SystemNotifications(Notifications):
    system = models.BooleanField(default = True)

    class Meta:
        db_table = 'System Notifications'

class UserNotifications(Notifications):
    user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)

    class Meta:
        db_table = 'User Notifications'

class ClubNotifications(Notifications):
    club = models.ForeignKey(Club, on_delete = models.CASCADE)

    class Meta:
        db_table = 'Club Notifications'