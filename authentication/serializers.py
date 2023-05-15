from rest_framework import serializers
from .models import User, Warn
from feeds.models import Feed
from commentary.models import Commentary

class WarnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warn
        fields = ('id', 'reason',)

class FeedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feed
        fields = ('id', 'text', 'published_date')

class CommentarySerializer(serializers.ModelSerializer):

    feed = FeedSerializer(read_only=True, many=False)

    class Meta:
        model = Commentary
        fields = ('id', 'text', 'published_date', 'feed')


class UserSerializer(serializers.ModelSerializer):

    feeds = FeedSerializer(read_only=True, many=True)
    commentaries = CommentarySerializer(read_only=True, many=True)
    warns = WarnSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'warns', 'feeds', 'commentaries')
