from django.shortcuts import render
from posts.models import Post, Comment
from users.models import User
iufgiyhlfvhy6i

def index1(request, username=None):
    if username:
        try:
            userr = User.objects.get(user_name=username)
            postss = Post.objects.filter(user=userr)
        except User.DoesNotExist:

            users_id = int(str(*list(User.objects.filter(user_name=username[1:-1]).values_list("id", flat=True))))
            postss = list(Post.objects.filter(id=users_id).values())


            #postss = User.objects.values_list("user_name", 'id', flat=True)
    else:
        postss = Post.objects.all()
    context = {"posts": postss, "title": "List of posts"}
    return render(request, 'posts/posts_lists.html', context)


def index2(request):
    comments = Comment.objects.all()
    context = {"comments": comments, "title": "List of comments"}
    return render(request, "posts/comments_lists.html", context)


