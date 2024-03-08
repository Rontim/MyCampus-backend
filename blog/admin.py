from django.contrib import admin
from .models import Blog
from comments.models import BlogComment
from comments.models import ReplyComment


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_user', 'author_club',
                    'created_at', 'updated_at')
    list_filter = ('author_user', 'author_club',
                   'created_at', 'updated_at')
    search_fields = ('title', 'author_user', 'author_club', 'content')
    ordering = ('title', 'author_user', 'author_club',
                'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('commentor', 'blog', 'comment', 'created_at', 'updated_at')
    list_filter = ('commentor', 'blog', 'comment')
    ordering = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(ReplyComment)
class ReplyComment(admin.ModelAdmin):
    list_display = ('replier', 'reply', 'comment', 'created_at', 'updated_at')
    list_filter = ('replier', 'reply', 'comment')
    ordering = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
