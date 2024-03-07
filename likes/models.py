from django.db import models
from blog.models import Blog
from django.contrib.auth import get_user_model

User = get_user_model()


class BlogLike(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, to_field="slug")
    user = models.ForeignKey(User, related_name='user_blog_likes',
                             on_delete=models.CASCADE, to_field='username')
    like_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Blog likes'
        constraints = [
            models.constraints.UniqueConstraint(
                fields=['user', 'blog'],
                name='unique_user_userblog_like'
            )
        ]
