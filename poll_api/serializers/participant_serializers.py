from rest_framework import serializers
from poll_api.models import Participant


class ParticipantListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participant
        fields = ['id', 'user', 'poll', 'pseudo']


class ParticipantDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participant
        fields = ['id', 'user', 'poll', 'pseudo']
