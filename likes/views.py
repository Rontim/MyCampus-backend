from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404

from blog.models import UserBlog, ClubBlog
from .models import ClubBlogLike, UserBlogLike

from .serializers import ClubBlogLikeSerializer, UserBlogLikeSerializer
from blog.serializers import ClubBlog, UserBlog


class Like(APIView):
    def get_clubblog(self, slug):
        try:
            blog = ClubBlog.objects.get(slug=slug)
        except ClubBlog.DoesNotExist:
            raise NotFound

    def get_userblog(self, slug):
        try:
            blog = UserBlog.objects.get(slug=slug)
        except UserBlog.DoesNotExist:
            raise NotFound

    def post(self, request, slug):
        print(slug)
        blog_type = request.data.get('author_type')

        blog = get_object_or_404(UserBlog, slug=slug)

        print(blog)

        if blog_type == 'user' and blog:
            like = UserBlogLike(user=request.user, blog=blog)
            like.save()
            return Response({'success': f'You have successfully liked this blog'})

        return Response({"detail": "failed to like this blog"}, status=status.HTTP_400_BAD_REQUEST)


class Unlike(APIView):
    def get_clubblog_like(self, slug, user):
        try:
            like = ClubBlogLike.objects.get(user=user.username, blog=slug)
        except ClubBlogLike.DoesNotExist:
            return None

    def get_userblog_like(self, slug, user):
        try:
            like = UserBlogLike.objects.get(user=user.username, blog=slug)
        except UserBlogLike.DoesNotExist:
            return None

    def get_like(self, slug, user):
        like = self.get_clubblog_like(
            slug=slug, user=user) or self.get_userblog_like(slug=slug, user=user)
        if not like:
            return NotFound
        return like

    def post(self, request, slug):
        user = request.user
        like = self.get_like(slug=slug, user=user)

        like.delete()  # type: ignore

        return Response({'success': f'You have successfully unliked'})
