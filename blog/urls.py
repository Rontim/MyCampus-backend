from django.urls import path
from .views import BlogsListView, CreateBlog, ReadBlog, BlogsByAuthor

urlpatterns = [
    path('create', CreateBlog.as_view()),
    path('<slug:slug>', ReadBlog.as_view()),
    path('', BlogsListView.as_view()),
    path('<str:author_type>/<str:author>/', BlogsByAuthor.as_view())
]
