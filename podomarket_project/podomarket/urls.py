from django.urls import path
from .views import *

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("posts/<int:post_id>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
]