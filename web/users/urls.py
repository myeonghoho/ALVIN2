from django.urls import path
from users import views

app_name = "users"
urlpatterns = [
    path("post/", views.post, name="post"),
    path("post_add/", views.post_add, name="post_add"),
    path("<int:post_id>/", views.post_detail, name="post_detail"),
    path("post_search/", views.post_search, name="post_search"),
]