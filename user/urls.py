from django.urls import path
from .views import AddUserInterests, GetSUserProfile

urlpatterns = [
    path('interests', AddUserInterests.as_view()),
]
