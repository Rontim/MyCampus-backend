from os import name
from re import T
from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model
from club.models import Club
import topic
from topic.models import Topic

User = get_user_model()


class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    thumbnail = models.ImageField(
        upload_to='blog/thumbnails/', null=True, blank=True)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserBlog(Blog):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name=f'blogs_{User.__name__.lower()}', name='author')
    topics = models.ManyToManyField(
        Topic, related_name=f'user_blogs_{Topic.__name__.lower()}', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'User Blog'
        verbose_name_plural = ('User Blogs')


class ClubBlog(Blog):
    author = models.ForeignKey(
        Club, on_delete=models.CASCADE, related_name=f'blogs_{Club.__name__.lower()}')
    topics = models.ManyToManyField(
        Topic, related_name=f'club_blogs_{Topic.__name__.lower()}')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Club Blog'
        verbose_name_plural = ('Club Blogs')
