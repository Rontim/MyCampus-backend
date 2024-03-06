from django.urls import path
from .views import Like, Unlike



urlpatterns= [
    path('<slug:slug>/like', Like.as_view()),
    path('<slug:slug>/unlike', Unlike.as_view())
]