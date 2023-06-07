from .models import Post, Comment,  User
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import AnonymousUser
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.decorators import database_sync_to_async
from djangochannelsrestframework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    DeleteModelMixin,
)
from .online import Online


def post_to_json(model):
    return {'author': model.author.id, 'title': model.title, 'text': model.text,
                        'created_at': model.created_at}


def comment_to_json(model):
    return {'content': model.content,
                        'to_post': model.to_post.id}


class GetPosts(Online, GenericAsyncAPIConsumer, ListModelMixin):
    serializer_class = PostSerializer

    def get_queryset(self, **kwargs):
        posts = Post.objects.filter(author=self.scope['user'])
        return posts


class PostCreate(Online, CreateModelMixin, GenericAsyncAPIConsumer):
    serializer_class = PostSerializer

    def perform_create(self, serializer, **kwargs):
        return Post.objects.create(title=serializer.data.get('title'), text=serializer.data.get('text'), author=self.scope['user'])


class PostDelete(Online, GenericAsyncAPIConsumer, DeleteModelMixin):
    permission_classes = (IsAuthenticated, )

    def get_queryset(self, **kwargs):
        return Post.objects.filter(author=self.scope['user'])


class CommentCreate(Online, CreateModelMixin, GenericAsyncAPIConsumer):
    serializer_class = CommentSerializer

    def perform_create(self, serializer, **kwargs):
        return Comment.objects.create(content=serializer.data.get('content'), to_post=Post.objects.get(id=serializer.data.get('to_post')), owner=self.scope['user'])


class CommentDelete(Online, GenericAsyncAPIConsumer, DeleteModelMixin):
    permission_classes = (IsAuthenticated, )

    def get_queryset(self, **kwargs):
        return Comment.objects.filter(owner=self.scope['user'])