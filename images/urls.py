from django.urls import path
from .views import ImageView

urlpatterns = [
    path('upload', ImageView.as_view())
]
