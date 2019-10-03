# The washes serializers

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Washes


class WashesSerializer(serializers.ModelSerializer):
    # Should we be using nested serializers here?
    tools = serializers.PrimaryKeyRelatedField(
            many=True,
            read_only=True)

    class Meta:
        model = Washes
        fields = ('id', 'title', 'date_created', 'tools', 'owner')


class WashesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Washes
        # Owner is injected at the time of creation by overriding
        # the perfrom_create() method in the corresponding view.
        # It's set to the current user that's authenticated
        fields = ('id', 'title', 'date_created', 'tools')


class WashDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Washes
        fields = ('id', 'title', 'date_created', 'tools', 'owner')
