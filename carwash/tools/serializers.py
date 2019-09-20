# The tools serializers
from rest_framework import serializers
from .models import Tools


class ToolsSerializer(serializers.ModelSerializer):
    wash = serializers.PrimaryKeyRelatedField(
            many=True,
            read_only=True)

    class Meta:
        model = Tools
        fields = ['name', 'brand', 'use', 'wash']
