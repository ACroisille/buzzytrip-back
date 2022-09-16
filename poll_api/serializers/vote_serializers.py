from rest_framework import serializers
from poll_api.models import Vote


class VoteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'is_pos']


class VoteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'is_pos']