from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from carwash.serializers import UserSerializer, GroupSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
import pdb
from rest_framework.response import Response
from rest_framework import generics

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class LoginView(generics.CreateAPIView):
    """
    Check the credentials and return the JWT Token
    if the credentials are valid and authenticated.
    """

    permission_classes = []
    serializer_class = LoginSerializer


    def login(self):
        username = self.serializer.validated_data['username']
        self.user = User.objects.get(username=username)
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh)
        self.access_token = str(refresh.access_token)

    def get_response(self):

        data = {
            'user': self.user,
            'token': self.token,
            'access': self.access_token
        }
        serializer = self.serializer_class(instance=data,
                                      context={'request': self.request})
        response = Response(serializer.validated_data, status=status.HTTP_200_OK) 


    def post(self, request, *args, **kwargs):
        """
        This view should receive a username and password when
        POSTing
        """
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data,
                                              context={'request': request})
        self.serializer.is_valid(raise_exception=True)

        self.login()
        return self.get_response()

