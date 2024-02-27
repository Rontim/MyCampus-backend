from pickle import TRUE
from unittest.util import _MAX_LENGTH
from django.db import models


class Topic (models.Model):
    slug=models.SlugField(max_length=255, unique=True, blank=True, null=True)
    topic_name=models.CharField(max_length=255)
    
    def __str__(self):
        return self.topic_name