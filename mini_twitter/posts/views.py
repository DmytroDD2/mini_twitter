from django.shortcuts import render
from posts.models import Post, Comment
from users.models import User


def index1(request, username=None):
    if username:
        try:
            userr = User.objects.get(user_name=username)
            postss = Post.objects.filter(user=userr)
        except User.DoesNotExist:
            postss = []
    else:
        postss = Post.objects.all()
    context = {"posts": postss, "title": "List of posts"}
    return render(request, 'posts/posts_lists.html', context)


def index2(request):
    comments = Comment.objects.all()
    context = {"comments": comments, "title": "List of comments"}
    return render(request, "posts/comments_lists.html", context)


