from rest_framework.viewsets import ModelViewSet

from poll_api.models import User, Poll, Participant
from poll_api.serializers import UserSerializer, PollSerializer, ParticipantSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()


class PollViewSet(ModelViewSet):
    serializer_class = PollSerializer

    def get_queryset(self):
        return Poll.objects.all()


class ParticipantViewSet(ModelViewSet):
    serializer_class = ParticipantSerializer

    def get_queryset(self):
        queryset = Participant.objects.all()
        user_id = self.request.GET.get('user_id')
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)

        return queryset
