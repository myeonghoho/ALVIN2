from django.urls import path
from users import views

app_name = "users"
urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("post_add/", views.post_add, name="post_add"),
]