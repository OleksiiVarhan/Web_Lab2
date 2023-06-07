from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    online = models.BooleanField(default=False)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    to_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')



