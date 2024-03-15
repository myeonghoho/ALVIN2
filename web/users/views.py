from django.shortcuts import render

# Create your views here.

def login_view(request):
    return render(request, "users/login.html")

def post_add(request):
    return render(request, "users/post_add.html")