from rest_framework import serializers
from .models import Feed
from authentication.serializers import UserSerializer
from commentary.serializers import CommentarySerializer

class FeedSerializer(serializers.ModelSerializer):

    author = UserSerializer(read_only=True, many=False)
    commentaries = CommentarySerializer(read_only=True, many=True)

    class Meta:
        model = Feed
        fields = ('id', 'text', 'published_date', 'author', 'commentaries')