from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404

from blog.models import Blog
from .models import BlogLike

from .serializers import BlogLikeSerializer
from blog.serializers import BlogCreateRetrieveSerializer, BlogListingSerializer


class Like(APIView):
    def get_blog(self, slug):
        try:
            blog = Blog.objects.get(slug=slug)
        except Blog.DoesNotExist:
            raise NotFound
        return blog

    def post(self, request, slug):
        blog = self.get_blog(slug=slug)
        user = request.user

        serializer = BlogLikeSerializer(data={
            'blog': blog.slug,
            'user': user.username
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'success': f'You have successfully liked {blog.title}'})


class Unlike(APIView):
    def get_like(self, slug, user):
        blog = get_object_or_404(Blog, slug=slug)
        like = get_object_or_404(BlogLike, blog=blog, user=user)

        return like

    def post(self, request, slug):
        user = request.user
        like = self.get_like(slug=slug, user=user)

        like.delete()  # type: ignore

        return Response({'success': f'You have successfully unliked'})
