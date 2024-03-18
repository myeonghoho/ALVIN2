from django.urls import path
from nature import views


app_name = "nature"
urlpatterns = [
    path("typhoon/", views.typhoon_page, name="typhoon"),
    path("earthquake/", views.earthquake_page, name="earthquake"),
    path("fires/", views.fires_page, name="fires"),
    path("landslide/", views.landslide_page, name="landslide"),
    path("post/", views.post, name="post"),
]