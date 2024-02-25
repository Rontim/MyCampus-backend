from pickle import TRUE
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Club (models.Model):
    slug=models.SlugField(max_length=255, unique=True, blank=True, null=True)
    club_name=models.CharField(max_length=255)
    description=models.TextField()
    def __str__(self):
        return self.club_name