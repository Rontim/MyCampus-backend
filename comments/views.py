from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, exceptions
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from .models import BlogComment
from .serializers import CommentSerializer, ReplySerializer, CommentListSerializer
from blog.models import Blog
from django.contrib.auth import get_user_model

User = get_user_model()

class CommentAPIView(APIView):
    def get_blog(self, slug):
        try:
            return Blog.objects.get(slug=slug)
        except Blog.DoesNotExist:
            raise exceptions.NotFound("Blog not found.")

    def post(self, request):
        user = request.user
        blog_slug = request.data.get('blog_slug')
        comment_text = request.data.get('comment')
        mentions = request.data.get('mentions', [])

        blog = self.get_blog(slug=blog_slug)

        data = {
            'comment': comment_text,
            'commentor': user.username,
            'blog': blog.slug
        }

        serializer = CommentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReplyAPIView(APIView):
    def get_comment(self, uuid):
        return get_object_or_404(BlogComment, unique_id=uuid)

    def post(self, request, uuid):
        user = request.user
        reply_text = request.data.get('reply')

        comment = self.get_comment(uuid=uuid)

        data = {
            'replier': user.username,
            'comment': comment.unique_id,
            'reply': reply_text
        }

        serializer = ReplySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentDetailAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, uuid):
        comment = get_object_or_404(BlogComment, unique_id=uuid)
        serializer = CommentListSerializer(comment)
        return Response(serializer.data)
