from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from poll_api.models import Vote
from poll_api.serializers import VoteListSerializer, VoteDetailSerializer


class VoteViewSet(ModelViewSet):
    """
    Vote endpoint
    """
    permission_classes = (IsAuthenticated,)

    serializer_class = VoteListSerializer
    detail_serializer_class = VoteDetailSerializer

    def get_queryset(self):
        poll_id = self.request.query_params.get('poll_id')
        if poll_id:
            return Vote.objects.filter(participant__poll__id=poll_id)

        choice_id = self.request.query_params.get('choice_id')
        if choice_id:
            return Vote.objects.filter(choice__id=choice_id)

        return Vote.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()