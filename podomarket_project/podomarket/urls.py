from django.urls import path
from .views import *

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("posts/<int:post_id>", PostDetailView.as_view(), name="post-detail"),
    path("posts/new/", PostCreateView.as_view(), name="post-create"),
    path("posts/<int:post_id>/edit/", PostUpdateView.as_view(), name="post-update"),
    path("posts/<int:post_id>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path('users/<int:user_id>/', ProfileView.as_view(), name="profile"),
    path("users/<int:user_id>/posts", UserPostListView.as_view(), name="user-post"),
]