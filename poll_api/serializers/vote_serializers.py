from rest_framework import serializers
from poll_api.models import Vote


class VoteListSerializer(serializers.ModelSerializer):
    """
    /vote serializer
    """

    class Meta:
        model = Vote
        fields = ['id', 'is_pos', 'participant', 'choice']


class VoteDetailSerializer(serializers.ModelSerializer):
    """
    /vote/id serializer
    """

    class Meta:
        model = Vote
        fields = ['id', 'is_pos']