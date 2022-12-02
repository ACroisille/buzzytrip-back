from rest_framework import serializers
from rest_framework.fields import CharField

from poll_api.models import Poll, Participant


class PollListSerializer(serializers.ModelSerializer):
    """
    /poll serializer
    """
    pseudo = CharField(write_only=True, allow_null=True)

    class Meta:
        model = Poll
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'closing_time', 'participants', 'created_by',
                  'pseudo']

    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        if start_date and end_date and start_date > end_date:
            raise serializers.ValidationError('Finish must occur after start')

        return data

    def create(self, validated_data):
        """
        Poll object creation
        :param validated_data:
        :return: Poll
        """
        pseudo = validated_data.pop('pseudo', None)
        poll = Poll.objects.create(**validated_data)
        pseudo = pseudo if pseudo else poll.created_by.username
        Participant.objects.create(
            poll=poll, user=poll.created_by, pseudo=pseudo)

        return poll


class PollDetailSerializer(serializers.ModelSerializer):
    """
    /poll/id serializer
    """

    class Meta:
        model = Poll
        fields = ['id', 'name', 'description', 'start_date',
                  'end_date', 'closing_time', 'participants', 'created_by']
