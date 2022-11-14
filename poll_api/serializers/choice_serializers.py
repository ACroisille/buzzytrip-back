from rest_framework import serializers
from poll_api.models import Choice
from poll_api.serializers.vote_serializers import VoteListSerializer


class ChoiceListSerializer(serializers.ModelSerializer):
    votes = VoteListSerializer(many=True, read_only=True)

    class Meta:
        model = Choice
        fields = ['id', 'name', 'description', 'participant', 'votes']


class ChoiceDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ['id', 'name', 'description', 'participant', 'votes']

