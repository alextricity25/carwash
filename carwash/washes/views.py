from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

from .models import Washes
from .serializers import WashesSerializer

class WashesList(generics.ListAPIView):
    queryset = Washes.objects.all()
    serializer_class = WashesSerializer


