from rest_framework.viewsets import ModelViewSet

from poll_api.models import User, Poll, Participant, Choice, Vote
from poll_api.serializers import *


class UserViewSet(ModelViewSet):
    serializer_class = UserListSerializer
    detail_serializer_class = UserDetailSerializer

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class PollViewSet(ModelViewSet):
    serializer_class = PollListSerializer
    detail_serializer_class = PollDetailSerializer

    def get_queryset(self):
        return Poll.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


"""class ParticipantViewSet(ModelViewSet):
    serializer_class = ParticipantListSerializer
    detail_serializer_class = ParticipantDetailSerializer

    def get_queryset(self):
        return Participant.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class ChoiceViewSet(ModelViewSet):
    serializer_class = ChoiceListSerializer
    detail_serializer_class = ChoiceDetailSerializer

    def get_queryset(self):
        return Choice.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class VoteViewSet(ModelViewSet):
    serializer_class = VoteListSerializer
    detail_serializer_class = VoteDetailSerializer

    def get_queryset(self):
        return Vote.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()"""
