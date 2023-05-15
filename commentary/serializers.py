from rest_framework import serializers
from .models import Commentary
from authentication.serializers import UserSerializer

class CommentarySerializer(serializers.ModelSerializer):

    author = UserSerializer(read_only=True, many=False)
    class Meta:
        model = Commentary
        fields = ('id', 'text', 'published_date', 'author')