from datetime import datetime, timedelta
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
from club.models import Club
import topic
from topic.models import Topic

User = get_user_model()


# class BlogModel(models.Manager):
#     def period(self, period: str):

#         if period:
#             if period == 'today':
#                 queryset = queryset..period(today).filter(
#                     created_at__date=datetime.now().date)

#             elif period == 'this_week':
#                 today = datetime.now().date()
#                 start_date = today - timedelta(days=today.weekday())
#                 end_date = start_date + timedelta(days=6)
#                 queryset = queryset.filter(
#                     created_at__range=[start_date, end_date])
#             elif period == 'this_month':
#                 current_month = datetime.now().month
#                 current_year = datetime.now().year
#                 queryset = queryset.filter(
#                     created_at__month=current_month, created_at__year=current_year)

#             elif period == 'this_year':
#                 current_year = datetime.now().year
#                 queryset = queryset.filter(created_at__year=current_year)


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
    likes = models.IntegerField(default=0)


    def save(self, *args, **kwargs):
        base_slug = self.title
        if self.author_type == "user" and self.author_user:
            base_slug += f' {self.author_user.get_username()}'
        elif self.author_type == "club" and self.author_club:
            base_slug += f' {self.author_club.club_name}'
        self.slug = slugify(base_slug)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'Title: {self.title}\nAuthor: {self.author_user if self.author_user else self.author_club}'

    @property
    def author(self):
        if self.author_user:
            return self.author_user
        else:
            return self.author_club

    def add_likes(self):
        self.likes += 1
        self.save()

    def remove_likes(self):
        self.likes -= 1
        self.save()

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        db_table = 'Blog'
