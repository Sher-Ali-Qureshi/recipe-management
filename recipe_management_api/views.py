from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework import status
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from recipe_management_api import serializer
from recipe_management_api import models
from recipe_management_api import permissions



class HelloAPiView(APIView):
    """Test Api"""

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview=[
            'User HTTP',
            'user HTTP',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profile"""
    serializer_class = serializer.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

class UserLoginApiView(ObtainAuthToken):
    """Handle create user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



class UserRecipeViewSet(viewsets.ModelViewSet):
    """Handle creating, reading and updating profile  feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializer.UserRecipeSerializer
    queryset = models.UserRecipe.objects.all()
    permission_classes = (
        permissions.UpdateOwnRecipe,
        IsAuthenticated
    )

    def perform_create(self, serializer):
        """Set the user profile to logged in user"""
        serializer.save(user_profile=self.request.user)

class ChangePasswordView(generics.UpdateAPIView):

    queryset = models.UserProfile.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = serializer.ChangePasswordSerializer
