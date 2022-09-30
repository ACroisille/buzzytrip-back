from rest_framework.viewsets import ModelViewSet

from poll_api.models import Vote
from poll_api.serializers import VoteListSerializer, VoteDetailSerializer


class VoteViewSet(ModelViewSet):
    serializer_class = VoteListSerializer
    detail_serializer_class = VoteDetailSerializer

    def get_queryset(self):
        return Vote.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()