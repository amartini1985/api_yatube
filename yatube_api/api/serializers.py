from django.contrib.auth import get_user_model
from rest_framework import serializers

from posts.models import Comment, Group, Post

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        required=False,
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Post
        fields = ('__all__')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('__all__')
        read_only_fields = ('posts',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        required=False,
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Comment
        fields = ('__all__')
        read_only_fields = ('post',)
