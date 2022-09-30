from rest_framework.viewsets import ModelViewSet

from poll_api.models import Participant
from poll_api.serializers import ParticipantListSerializer, ParticipantDetailSerializer


class ParticipantViewSet(ModelViewSet):
    serializer_class = ParticipantListSerializer
    detail_serializer_class = ParticipantDetailSerializer

    def get_queryset(self):
        return Participant.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()