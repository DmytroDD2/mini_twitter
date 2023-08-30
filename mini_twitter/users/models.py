from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=250)
    date_joined = models.DateField(auto_now_add=True)

    crea_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
