from rest_framework import serializers
from poll_api.models import Choice
from poll_api.serializers.vote_serializers import VoteListSerializer


class ChoiceListSerializer(serializers.ModelSerializer):
    """
    /choice serializer
    """
    votes = VoteListSerializer(many=True, read_only=True)

    class Meta:
        model = Choice
        fields = ['id', 'name', 'description', 'link',
                  'creation_time', 'participant', 'votes']


class ChoiceDetailSerializer(serializers.ModelSerializer):
    """
    /choice/id serializer
    """

    class Meta:
        model = Choice
        fields = ['id', 'name', 'description', 'link',
                  'creation_time', 'participant', 'votes']
