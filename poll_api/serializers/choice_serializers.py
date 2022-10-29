from rest_framework import serializers
from poll_api.models import Choice


class ChoiceListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ['id', 'name', 'description', 'participant', 'votes']
        read_only_fields = ['votes']


class ChoiceDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ['id', 'name', 'description', 'participant', 'votes']

