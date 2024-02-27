from django.urls import path
from .views import TopicView, TopicList

urlpatterns= [
    path('<slug:slug>/', TopicView.as_view()),
    path('list', TopicList.as_view())
]