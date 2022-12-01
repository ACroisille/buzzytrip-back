from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from poll_api.models import Choice
from poll_api.serializers import ChoiceListSerializer, ChoiceDetailSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ChoiceViewSet(ModelViewSet):
    """
    Choice endpoint
    """
    permission_classes = (IsAuthenticated,)

    serializer_class = ChoiceListSerializer
    detail_serializer_class = ChoiceDetailSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        poll_id = self.request.query_params.get('poll_id')
        if poll_id:
            return Choice.objects.filter(participant__poll__id=poll_id)

        return Choice.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()