from django.urls import path
from posts.views import index1, index2

urlpatterns = [
    path('', index1, name="posts"),
    path('comments/', index2, name="comments"),
    path('<str:username>/', index1, name="user_comments")
]

