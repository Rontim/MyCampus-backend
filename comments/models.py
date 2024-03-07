from django import db
from django.db import models
from blog.models import Blog
from django.contrib.auth import get_user_model
import uuid


def generate_uuid():
    return uuid.uuid4().hex

User = get_user_model()

class BlogComment(models.Model):
    unique_id = models.CharField(
        default=generate_uuid, max_length=200, unique=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, to_field='slug')
    commentor = models.ForeignKey(
        User, on_delete=models.CASCADE, to_field='username')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Blog_comments'
        verbose_name = 'Blog Comment'
        verbose_name_plural = 'Blog Comments'

    def __str__(self):
        return f'{self.commentor} commented on {self.blog.title} at {self.created_at}'


class ReplyComment(models.Model):
    unique_id = models.CharField(
        default=generate_uuid, max_length=200, unique=True)
    comment = models.ForeignKey(
        BlogComment, on_delete=models.CASCADE, related_name='replies', to_field='unique_id')
    replier = models.ForeignKey(
        User, on_delete=models.CASCADE, to_field='username')
    reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Reply_comments'
        verbose_name = 'Reply Comment'
        verbose_name_plural = 'Reply Comments'

    def __str__(self):
        return f'{self.replier} replied to {self.comment.commentor}\'s comment at {self.created_at}'

