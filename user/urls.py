from django.urls import path
from .views import AddUserInterests

urlpatterns = [
    path('interests', AddUserInterests.as_view()),

]
