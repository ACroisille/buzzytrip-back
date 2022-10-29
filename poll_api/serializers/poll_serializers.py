from rest_framework import serializers
from poll_api.models import Poll, Participant
from poll_api.serializers.participant_serializers import ParticipantDetailSerializer, ParticipantListSerializer


class PollListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = ['id', 'name', 'description', 'participants', 'created_by']


class PollDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = ['id', 'name', 'description', 'participants', 'created_by']
