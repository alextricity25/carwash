from django.shortcuts import render
from rest_framework import generics

from .models import Tools
from .serializers import ToolsSerializer

class ToolsList(generics.ListAPIView):
    queryset = Tools.objects.all()
    serializer_class = ToolsSerializer



