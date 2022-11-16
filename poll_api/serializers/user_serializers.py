from rest_framework import serializers

from poll_api.models import User


class UserListSerializer(serializers.ModelSerializer):
    """
    /user serializer
    """

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'polls']


class UserDetailSerializer(serializers.ModelSerializer):
    """
    /user/id serializer
    """

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
