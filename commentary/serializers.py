from rest_framework import serializers
from .models import Commentary
from authentication.models import User
from feeds.models import Feed

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email')

class FeedSerializer(serializers.ModelSerializer):

    author = UserSerializer(read_only=True, many=False)
    class Meta:
        model = Feed
        fields = ('id', 'text', 'author')

class CommentarySerializer(serializers.ModelSerializer):

    feed = FeedSerializer(read_only=True, many=False)
    author = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Commentary
        fields = ('id', 'text', 'published_date', 'author', 'feed')