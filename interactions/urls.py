from django.urls import path
from .views import FollowUser, FollowClub, UnfollowUser, UnfollowClub

urlpatterns = [
    path('club/follow', FollowClub.as_view()),
    path('user/follow', FollowUser.as_view()),
    path('club/unfollow', UnfollowClub.as_view()),
    path('user/unfollow', UnfollowUser.as_view())
]
