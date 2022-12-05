from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from poll_api.models import Participant, Vote
from poll_api.serializers import ParticipantListSerializer, ParticipantDetailSerializer


class ParticipantViewSet(ModelViewSet):
    """
    Participant endpoint
    """
    permission_classes = (IsAuthenticated,)

    serializer_class = ParticipantListSerializer
    detail_serializer_class = ParticipantDetailSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        poll_id = self.request.query_params.get('poll_id')

        if user_id and poll_id:
            return Participant.objects.filter(user=user_id, poll=poll_id)
        if poll_id:
            return Participant.objects.filter(poll__id=poll_id)

        return Participant.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

    @action(detail=True, url_path='get_vote_count', url_name='get_vote_count')
    def get_vote_count(self, request, pk=None):
        participant = self.get_object()
        votes = Vote.objects.filter(participant=participant)

        response = {
            'participant_id': participant.id,
            'vote_count': len(votes)
        }

        return Response(response)
