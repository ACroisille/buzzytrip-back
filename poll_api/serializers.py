from rest_framework.serializers import ModelSerializer
from poll_api.models import User, Poll, Participant


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']


class PollSerializer(ModelSerializer):
    participants = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Poll
        fields = ['id', 'name', 'description', 'participants']


class ParticipantSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    poll = PollSerializer(read_only=True)

    class Meta:
        model = Participant
        fields = ['id', 'pseudo', 'user', 'poll']

