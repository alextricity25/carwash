# The washes serializers

#from django.contrib.auth.models import User
from rest_framework import serializers
from tools.models import Tools
from .models import Washes

class WashesSerializer(serializers.ModelSerializer):
    tools = serializers.StringRelatedField(
            many = True,
            read_only = True)

    class Meta:

        model = Washes
        fields = ('id', 'title', 'date_created', 'tools')
