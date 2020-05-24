from rest_framework import status
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

from django.db.utils import ProgrammingError
from django.http import Http404
from django.contrib.auth.models import User

from places import helper
from places.models import State, Locality, LocalityClassAut, GeocodeReliabilityAut
from places.serializers import StateSerializer, UserSerializer, \
    LocalitySerializer, LocalityClassAutSerializer, \
    GeocodeReliabilityAutSerializer, AddressSerializer


class APIRoot(APIView):
    """
    API root view
    """
    def get(self, request, format=None):
        return Response({'documentation': reverse('swagger-ui', request=request, format=format)})


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
    State view set
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
    Locality class aut view set
    """
    queryset = LocalityClassAut.objects.all()
    serializer_class = LocalityClassAutSerializer
    permission_classes = [permissions.IsAuthenticated]


class GeocodeReliabilityAutViewSet(viewsets.ModelViewSet):
    """
    Geocode reliability aut view set
    """
    queryset = GeocodeReliabilityAut.objects.all()
    serializer_class = GeocodeReliabilityAutSerializer
    permission_classes = [permissions.IsAuthenticated]


class ParseAddressViewSet(mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    """
    Parse address view set
    """
    renderer_classes = [renderers.JSONRenderer,
                        renderers.BrowsableAPIRenderer]

    lookup_field = 'address'
    serializer_class = AddressSerializer

    def retrieve(self, request, address, *args, **kwargs):
        parsed_address = helper.parse_address(address)
        serializer = AddressSerializer(parsed_address)
        return Response(serializer.data)


class GeocodeAddressViewSet(mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """
    Geocode address view set
    """
    renderer_classes = [renderers.JSONRenderer,
                        renderers.BrowsableAPIRenderer]

    lookup_field = 'address'
    serializer_class = AddressSerializer

    def retrieve(self, request, address, *args, **kwargs):
        try:
            # geocode address
            geocoded_address = helper.geocode_address(address)
            serializer = AddressSerializer(geocoded_address)
            return Response(serializer.data)

        except ProgrammingError as pe:
            return Response({'detail': 'Geocode function not found. Install geocoder from https://github.com/william-librata/geocoder'},
                            status.HTTP_404_NOT_FOUND)
