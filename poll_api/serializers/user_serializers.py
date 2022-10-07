from rest_framework import serializers

from poll_api.models import User
from poll_api.serializers.poll_serializers import PollListSerializer, PollDetailSerializer


class UserListSerializer(serializers.ModelSerializer):
    polls = PollListSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'polls']


class UserDetailSerializer(serializers.ModelSerializer):
    polls = PollDetailSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'polls']
