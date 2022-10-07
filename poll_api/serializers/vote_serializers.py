from rest_framework import serializers
from poll_api.models import Vote


class VoteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'is_pos', 'participant', 'choice']


class VoteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'is_pos']