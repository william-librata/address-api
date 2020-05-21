from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.schemas.openapi import AutoSchema

from rest_framework.authentication import TokenAuthentication, SessionAuthentication

from django.http import Http404

from django.contrib.auth.models import User

from postal.parser import parse_address

from places.models import State, Locality, LocalityClassAut, GeocodeReliabilityAut
from places.serializers import StateSerializer, UserSerializer, \
    LocalitySerializer, LocalityClassAutSerializer, \
    GeocodeReliabilityAutSerializer


class UserList(APIView):
    """
    List all user
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        user = User.objects.all()
        import pdb;pdb.set_trace()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)


class UserDetail(APIView):
    """
    List a single user detail
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, username, format=None):
        user = self.get_object(username)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class StateViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = State.objects.all()
    serializer_class = StateSerializer
    #authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'state_pid'


class LocalityViewSet(viewsets.ModelViewSet):
    """
    Locality view set with list, create, retrieve, update and destroy
    """
    queryset = Locality.objects.\
        select_related('state_pid').\
        select_related('locality_class_code').\
        select_related('gnaf_reliability_code')
    serializer_class = LocalitySerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'locality_pid'


class LocalityClassAutViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = LocalityClassAut.objects.all()
    serializer_class = LocalityClassAutSerializer
    permission_classes = [permissions.IsAuthenticated]


class GeocodeReliabilityAutViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = GeocodeReliabilityAut.objects.all()
    serializer_class = GeocodeReliabilityAutSerializer
    permission_classes = [permissions.IsAuthenticated]

class ParseAddressView(APIView):
    renderer_classes = [renderers.JSONRenderer, renderers.BrowsableAPIRenderer]

    def get(self, request, address, format=None):
        # turn list into reverse dict
        parsed_address = dict((y, x) for x, y in parse_address(address))
        if parsed_address:
            Response(status.HTTP_404_NOT_FOUND)
        return Response(parsed_address, status.HTTP_200_OK)
