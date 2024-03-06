from django.db import models
from blog.models import UserBlog, ClubBlog
from django.contrib.auth import get_user_model

User = get_user_model()


class UserBlogLike(models.Model):
    blog = models.ForeignKey(UserBlog, on_delete=models.CASCADE, to_field="slug")
    user = models.ForeignKey(User, related_name = 'user_blog_likes', on_delete=models.CASCADE, to_field='username')
    like_time = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = 'UserBlog Like'
        constraints = [
            models.constraints.UniqueConstraint(
                fields=['user', 'blog'],
                name='unique_user_userblog_like'
            )
        ]


    
class ClubBlogLike(models.Model):
    blog = models.ForeignKey(ClubBlog, on_delete=models.CASCADE, to_field="slug")
    user = models.ForeignKey(User, related_name = 'club_blog_likes', on_delete=models.CASCADE, to_field='username')
    like_time = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = 'ClubBlog Like'
        constraints = [
            models.constraints.UniqueConstraint(
                fields=['user', 'blog'],
                name='unique_user_clubblog_like'
            )
        ]


