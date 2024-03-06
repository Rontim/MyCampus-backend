from django.db import models
from blog.models import ClubBlog, UserBlog
from django.contrib.auth import get_user_model

User = get_user_model()


class ClubBlogComment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, to_field='username')
    blog = models.ForeignKey(ClubBlog, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    mentions = models.ManyToManyField(User, related_name='mentions')

    def __str__(self):
        return f'Commented by {self.user} on {self.blog.title}'

    class Meta:
        ordering = ['-created_at']
        db_table = 'club_blog_comment'


class UserBlogComment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, to_field='username')
    blog = models.ForeignKey(UserBlog, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    mentions = models.ManyToManyField(User, related_name='mentions')

    def __str__(self):
        return f'Commented by {self.user} on {self.blog.title}'

    class Meta:
        ordering = ['-created_at']
        db_table = 'user_blog_comment'


class CommentClubBlogComment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, to_field='username')
    comment = models.ForeignKey(
        ClubBlogComment, on_delete=models.CASCADE, null=True, blank=True)
    comment_comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    mentions = models.ManyToManyField(User, related_name='mentions')

    def __str__(self):
        return f'Commented by {self.user} on {self.comment}'

    class Meta:
        ordering = ['-created_at']
        db_table = 'comment_clubblog_comment'


class CommentUserBlogComment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, to_field='username')
    comment = models.ForeignKey(
        UserBlogComment, on_delete=models.CASCADE, null=True, blank=True)
    comment_comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    mentions = models.ManyToManyField(User, related_name='mentions')

    def __str__(self):
        return f'Commented by {self.user} on {self.comment}'

    class Meta:
        ordering = ['-created_at']
        db_table = 'comment_userblog_comment'
