from django.shortcuts import render

# Create your views here.

def typhoon(request):
    return render(request, 'typhoon.html')

def earthquake(request):
    return render(request, 'earthquake.html')

def landslide(request):
    return render(request, 'landslide.html')


def fires(request):
    return render(request, 'fires.html')


def post(request):
    return render(request, 'post.html')

