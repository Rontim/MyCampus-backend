from user.views import GetSUserProfile
from blog.views import SearchBlogs, TrendingBlogs
from topic.views import TrendingTopics
from django.urls import path

urlpatterns = [
    path('topics/trending', TrendingTopics.as_view()),
    path('blogs/trending', TrendingBlogs.as_view()),
    path('blogs/search', SearchBlogs.as_view()),
    path('user/<str:username>', GetSUserProfile.as_view()),
]
