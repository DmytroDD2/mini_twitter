from django.shortcuts import render
from users.models import User



def index(request):
    users = User.objects.all()
    context = {"users": users, 'title': 'List of users'}
    return render(request, 'users/users_lists.html', context)

