from rest_framework import serializers
from poll_api.models import Participant
from poll_api.serializers.choice_serializers import ChoiceDetailSerializer


class ParticipantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['id', 'user', 'poll', 'pseudo']


class ParticipantDetailSerializer(serializers.ModelSerializer):
    choices = ChoiceDetailSerializer(many=True)
    # user = serializers.StringRelatedField()

    class Meta:
        model = Participant
        fields = ['id', 'user', 'poll', 'pseudo', 'choices']
