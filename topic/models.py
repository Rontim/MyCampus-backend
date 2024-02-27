from django.db import models
from django.template.defaultfilters import slugify


class Topic (models.Model):
    slug=models.SlugField(max_length=255, unique=True, blank=True, null=True)
    topic_name=models.CharField(max_length=255)
    
    def __str__(self):
        return self.topic_name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.topic_name)
        super().save(*args, **kwargs)