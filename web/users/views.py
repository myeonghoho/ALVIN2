from django.shortcuts import render

# Create your views here.
def post(request):
    posts = Post.objects.all() # 모든 Post객체를 가진 QuerySet

    # 템플릿에 전달할 딕셔너리
    context = {
        "posts" : posts,
    }
    return render(request, "post.html", context)

def login_view(request):
    return render(request, "users/login.html")

def post_add(request):
    return render(request, "users/post_add.html")