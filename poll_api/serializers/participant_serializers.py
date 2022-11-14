from rest_framework import serializers
from poll_api.models import Participant


class ParticipantListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participant
        fields = ['id', 'user', 'poll', 'pseudo']

    def create(self, validated_data):
        print(validated_data)
        pseudo = validated_data.get('pseudo')
        pseudo = pseudo if pseudo else validated_data.get('user').username
        participant = Participant.objects.create(user=validated_data.get('user'), poll=validated_data.get('poll'),
                                                 pseudo=pseudo)

        return participant


class ParticipantDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participant
        fields = ['id', 'user', 'poll', 'pseudo']
