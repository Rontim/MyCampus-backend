from django.urls import path
from .views import ClubView, ClubList

urlpatterns= [
    path('<slug:slug>/', ClubView.as_view()),
    path('list', ClubList.as_view())
]