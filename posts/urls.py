from django.urls import path
from django.urls import re_path

from . import consumers

socket_urlpatterns = [
    re_path("ws/posts", consumers.GetPosts.as_asgi()),
    re_path("ws/post_create", consumers.PostCreate.as_asgi()),
    re_path("ws/post_delete", consumers.PostDelete.as_asgi()),
    re_path("ws/comment_create", consumers.CommentCreate.as_asgi()),
    re_path("ws/comment_delete", consumers.CommentDelete.as_asgi()),
]
