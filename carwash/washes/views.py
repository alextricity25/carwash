from rest_framework import generics
from rest_framework.permissions import IsAuthenticated 

from .models import Washes
from .serializers import WashesSerializer


class WashesList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WashesSerializer

    def get_queryset(self):
        """
        This view should return a list of all the washes
        for the currently authenticated user.
        """
        user = self.request.user
        return Washes.objects.filter(owner=user)
