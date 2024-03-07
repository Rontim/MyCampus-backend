from os import name
from re import T
from tabnanny import verbose
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
from club.models import Club
import topic
from topic.models import Topic

User = get_user_model()


class Blog(models.Model):
    AUTHOR_TYPE_CHOICES = (
        ('user', 'User'),
        ('club', 'Club'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    thumbnail = models.ImageField(
        upload_to='blog/thumbnails/', null=True, blank=True)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author_type = models.CharField(
        max_length=20, choices=AUTHOR_TYPE_CHOICES, default='user')
    author_user = models.ForeignKey(
        User, to_field='username', on_delete=models.CASCADE, related_name='user_blogs', null=True, blank=True)
    author_club = models.ForeignKey(
        Club, to_field='slug', on_delete=models.CASCADE, related_name='club_blogs', null=True, blank=True)
    topics = models.ManyToManyField(Topic, related_name='blogs', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self) -> str:
        return f'Title: {self.title}\nAuthor: {self.author_user if self.author_user else self.author_club}'


    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        db_table = 'Blog'
