from rest_framework import generics
from rest_framework.permissions import IsAuthenticated 

from .models import Washes
from .serializers import WashesSerializer, WashDetailSerializer, WashesCreateSerializer

class WashesList(generics.ListAPIView):
    serializer_class = WashesSerializer

    def get_queryset(self):
        """
        This view should return a list of all the washes
        for the currently authenticated user.
        """
        user = self.request.user
        return Washes.objects.filter(owner=user)


class WashesCreate(generics.CreateAPIView):
    serializer_class = WashesCreateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class WashesDetail(generics.RetrieveAPIView):
    serializer_class = WashDetailSerializer

    def get_object(self):
        return Washes.objects.get(pk=self.kwargs['pk'])
