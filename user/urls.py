from django.urls import path
from .views import UserCreateView, UserUpdateView

urlpatterns = [
    path('', UserCreateView.as_view()),
    path('update', UserUpdateView.as_view()),
]
