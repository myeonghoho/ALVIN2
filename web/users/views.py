from django.shortcuts import render, redirect
from users.models import Post


# Create your views here.

def post(request):
    posts = Post.objects.all() # 모든 Post객체를 가진 QuerySet

    # 템플릿에 전달할 딕셔너리
    context = {
        "posts" : posts,
    }
    return render(request, "post.html", context)



def post_detail(request, post_id):
    post = Post.objects.get(id=post_id) # id값이 URL에서 받은 post_id 값인 Post객체
    if request.method == "POST":
        # textarea의 name 속성값(comment)을 가져옴
        comment_content = request.POST["comment"]
        
        # 전달된 comment 값으로 Comment 객체를 생성
        # Comment.objects.create(
        #     post=post,
        #     content=comment_content,
        # )
        # 1. GET 요청으로 글 상세 페이지를 보여주거나
        # 2. POST 요청으로 댓글이 생성되거나
        # 3. 두 경우 모두, 이 글의 상세 페이지를 보여주면 됨

    context = {
        "post" : post,
    }

    return render(request, "users/post_detail.html", context)

def post_search(request):
    # GET방식으로 전달된 데이터를 출력
    keyword = request.GET.get("keyword", None)
    print(keyword)

    if keyword: # keyword값이 주어진 경우
        # 이름에 전달받은 키워드 값이 포함된 버거를 검색
        posts = Post.objects.filter(name__contains=keyword)

    else: # keyword가 주어지지 않아, None이 할당된 경우
        posts = Post.objects.none() # 빈 QuerySet을 할당

    context = {
        "posts" : posts,
    }
    return render(request, "users/post_detail.html", context)

def post_add(request):
    if request.method == "POST": # method가 POST일 때
        title = request.POST["title"]
        content = request.POST["content"]
        author = request.POST["author"]

        post = Post.objects.create(
            title=title,
            content=content,
            author=author, # 이미지 파일을 게시글 객체 생성 시에 전달
        )
        return redirect(f"/users/{post.id}/")

    return render(request, "users/post_add.html")
