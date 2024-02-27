from django.db import models
from django.template.defaultfilters import slugify


class Club (models.Model):
    slug=models.SlugField(max_length=255, unique=True, blank=True, null=True)
    club_name=models.CharField(max_length=255)
    description=models.TextField()
    def __str__(self):
        return self.club_name
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.club_name)
        super().save(*args, **kwargs)