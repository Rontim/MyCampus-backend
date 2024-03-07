from django.urls import path
from .views import CommentAPIView, ReplyAPIView, CommentDetailAPIView

urlpatterns = [
    path('', CommentAPIView.as_view()),
    path('<str:uuid>/reply', ReplyAPIView.as_view()),
    path('<str:uuid>', CommentDetailAPIView.as_view())
]
