from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path('success/', views.confirm_signup, name='confirm_signup'),
    path("posts/", views.post, name="allpost"),
    path("create_post/", views.create_post, name="create_post"),
    path("posts/delete/<slug:post_slug>", views.delete_post, name="delete_post"),
    path("posts/<slug:post_slug>", views.post_detail, name="post_details"),
]
