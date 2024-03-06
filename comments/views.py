from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ClubBlogComment, UserBlogComment, CommentClubBlogComment, CommentUserBlogComment
from .serializers import ClubBlogCommentSerializer, UserBlogCommentSerializer, CommentClubBlogCommentSerializer, CommentUserBlogCommentSerializer
from django.contrib.auth import get_user_model
from blog.models import ClubBlog, UserBlog
from django.shortcuts import get_object_or_404

User = get_user_model()

# class Comment()
