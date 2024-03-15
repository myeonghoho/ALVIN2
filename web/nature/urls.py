from django.urls import path
from nature import views


app_name = "nature"
urlpatterns = [
    path("typhoon/", views.typhoon, name="typhoon"),
    path("earthquake/", views.earthquake, name="earthquake"),
    path("fires/", views.fires, name="fires"),
    path("landslide/", views.landslide, name="landslide"),
    path("post/", views.post, name="post"),
]