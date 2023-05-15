from rest_framework import serializers
from .models import User, Warn

class WarnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warn
        fields = ('id', 'reason',)

class UserSerializer(serializers.ModelSerializer):

    warns = WarnSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'warns')