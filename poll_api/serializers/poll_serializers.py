from rest_framework import serializers
from rest_framework.fields import CharField

from poll_api.models import Poll, Participant


class PollListSerializer(serializers.ModelSerializer):
    pseudo = CharField(write_only=True, allow_null=True)

    class Meta:
        model = Poll
        fields = ['id', 'name', 'description', 'participants', 'created_by', 'pseudo']

    def create(self, validated_data):
        pseudo = validated_data.pop('pseudo', None)
        poll = Poll.objects.create(**validated_data)
        Participant.objects.create(poll=poll, user=poll.created_by, pseudo=pseudo)

        return poll


class PollDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = ['id', 'name', 'description', 'participants', 'created_by']
