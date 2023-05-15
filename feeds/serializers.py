from rest_framework import serializers
from .models import Feed
from authentication.models import User
from commentary.models import Commentary

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email')

class CommentarySerializer(serializers.ModelSerializer):

    author = UserSerializer(read_only=True, many=False)
    class Meta:
        model = Commentary
        fields = ('id', 'text', 'author')

class FeedSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True, many=False)
    commentaries = CommentarySerializer(read_only=True, many=True)

    class Meta:
        model = Feed
        fields = ('id', 'text', 'published_date', 'author', 'commentaries')
