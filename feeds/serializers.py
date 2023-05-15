from rest_framework import serializers
from .models import Feed
from commentary.serializers import CommentarySerializer
from authentication.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email')

class FeedSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True, many=False)
    commentaries = CommentarySerializer(read_only=True, many=True)

    class Meta:
        model = Feed
        fields = ('id', 'text', 'published_date', 'author', 'commentaries')
