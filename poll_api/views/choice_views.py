from django.db.models import F
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response

from poll_api.models import Choice, Participant, Vote
from poll_api.serializers import ChoiceListSerializer, ChoiceDetailSerializer
from poll_api.serializers.participant_serializers import ParticipantListSerializer

sort_mapping = {
    'creation_time_asc': F('creation_time').asc(),
    'creation_time_desc': F('creation_time').desc(),
    'price_asc': F('price').asc(),
    'price_desc': F('price').desc(),
}


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 24
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
        sort = self.request.query_params.get('sort')

        queryset = Choice.objects.all()
        if poll_id:
            queryset = Choice.objects.filter(participant__poll__id=poll_id)
        if sort:
            queryset = queryset.order_by(sort_mapping[sort])

        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

    @action(detail=True, url_path='get_voters', url_name='get_voters')
    def get_voters(self, request, pk=None):
        choice = self.get_object()
        participants = Participant.objects.filter(
            votes__in=Vote.objects.filter(choice=choice))

        return Response(ParticipantListSerializer(participants, many=True).data)
