from django.urls import path
from .views import CreateBlog, ReadBlog

urlpatterns = [
    path('create', CreateBlog.as_view()),
    path('<slug:slug>', ReadBlog.as_view())
]
