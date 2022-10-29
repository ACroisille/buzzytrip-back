from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from poll_api.models import Choice
from poll_api.serializers import ChoiceListSerializer, ChoiceDetailSerializer


class ChoiceViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = ChoiceListSerializer
    detail_serializer_class = ChoiceDetailSerializer

    def get_queryset(self):
        poll_id = self.request.query_params.get('poll_id')
        if poll_id:
            return Choice.objects.filter(participant__poll__id=poll_id)

        return Choice.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()