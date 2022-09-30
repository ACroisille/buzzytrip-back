from rest_framework.viewsets import ModelViewSet

from poll_api.models import User
from poll_api.serializers import UserListSerializer, UserDetailSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserListSerializer
    detail_serializer_class = UserDetailSerializer

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()