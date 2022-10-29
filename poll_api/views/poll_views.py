from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from poll_api.models import Poll
from poll_api.serializers import PollListSerializer, PollDetailSerializer


class PollViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = PollListSerializer
    detail_serializer_class = PollDetailSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            return Poll.objects.filter(participant__user__id=user_id)
        return Poll.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()