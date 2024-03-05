from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from blog.models import UserBlog, ClubBlog
from .models import ClubBlogLike, UserBlogLike

from .serializers import ClubBlogLikeSerializer,UserBlogLikeSerializer
from blog.serializers import ClubBlog, UserBlog

class Like(APIView):
    def get_club_blog(self, slug):
      try:
        blog ={'blog': UserBlog.objects.get(slug=slug), 'table': 'club'}
      except UserBlog.DoesNotExist:
        return None
      return blog
      
    def get_user_blog(self, slug):
      try:
        blog = {'blog': ClubBlog.objects.get(slug=slug), 'table': 'user'}
      except ClubBlog.DoesNotExist:
        return None
      
    def get_club(self, slug):
      blog = self.get_club_blog(slug=slug) or self.get_user_blog(slug=slug)
      if not blog:
        raise NotFound
      return blog

    def post(self, request, slug):
        blog = self.get_club(slug=slug)

        user = request.user

        blog_kind = blog['table']
        blog = blog['blog']

        serializer = None

        if blog_kind == 'club':
            serializer = ClubBlogLikeSerializer(data={
            'user': user.username,
            'blog': blog.slug
            })
            serializer.is_valid(raise_exception=True)
            serializer.save()
        
        
        if blog_kind == 'club':
            serializer = UserBlogLikeSerializer(data={
            'user': user.username,
            'blog': blog.slug
            })
            serializer.is_valid(raise_exception=True)
            serializer.save()

        return Response({'success': f'You have successfully liked {blog.title}'})
    

class Unlike(APIView):
    def get_clubblog_like(self, slug, user):
        try:
           like = ClubBlogLike.objects.get(user = user.username, blog = slug)
        except ClubBlogLike.DoesNotExist:
           return None
        

    def get_userblog_like(self, slug, user):
        try:
          like = UserBlogLike.objects.get(user= user.username, blog = slug)
        except UserBlogLike.DoesNotExist:
          return None
        
    def get_like(self, slug, user):
       like = self.get_clubblog_like(slug=slug, user=user) or self.get_userblog_like(slug=slug, user=user)
       if not like:
          return NotFound
       return like
    
    def post(self, request, slug):
       user = request.user
       like = self.get_like(slug=slug, user=user)

       like.delete() # type: ignore

       return Response({'success': f'You have successfully unliked'})


       
        
       



        

      
         