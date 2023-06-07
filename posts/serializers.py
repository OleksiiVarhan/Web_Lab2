from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = self.context['request'].user
        post = Post.objects.create(title=validated_data.get('title'), text=validated_data.get('text'), author=user)
        return post

    class Meta:
        model = Post
        fields = ('title', 'text', )


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('content', 'to_post')

    def create(self, validated_data):
        user = self.context['request'].user
        comment = Comment.objects.create(content=validated_data.get('content'), owner=user,
                                         to_post=Post.objects.get(id=validated_data.get('to_post')))
        return comment