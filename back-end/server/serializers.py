from rest_framework import serializers
from .models import Posts, Comments
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['post_id', 'title', 'content']

class CommentsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    post = PostsSerializer()
    class Meta:
        model = Comments
        fields = ['comment_id', 'user_id', 'content', 'post_id']