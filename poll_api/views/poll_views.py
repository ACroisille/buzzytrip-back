from rest_framework.viewsets import ModelViewSet

from poll_api.models import Poll
from poll_api.serializers import PollListSerializer, PollDetailSerializer


class PollViewSet(ModelViewSet):
    serializer_class = PollListSerializer
    detail_serializer_class = PollDetailSerializer

    def get_queryset(self):
        return Poll.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()