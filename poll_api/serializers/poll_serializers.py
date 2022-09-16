from rest_framework import serializers
from poll_api.models import Poll, Participant
from poll_api.serializers.participant_serializers import ParticipantDetailSerializer, ParticipantListSerializer


class PollListSerializer(serializers.ModelSerializer):
    participants = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Poll
        fields = ['id', 'name', 'description', 'participants', 'created_by']

    def get_participants(self, instance):
        queryset = Participant.objects.filter(poll=instance.id)
        serializer = ParticipantListSerializer(queryset, many=True)
        return serializer.data


class PollDetailSerializer(serializers.ModelSerializer):
    participants = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Poll
        fields = ['id', 'name', 'description', 'participants', 'created_by']

    def get_participants(self, instance):
        queryset = Participant.objects.filter(poll=instance.id)
        serializer = ParticipantDetailSerializer(queryset, many=True)
        return serializer.data
