from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.schemas.openapi import AutoSchema

from django.http import Http404

from django.contrib.auth.models import User

from places.models import State, Locality, LocalityClassAut, GeocodeReliabilityAut
from places.serializers import StateSerializer, UserSerializer, \
    LocalitySerializer, LocalityClassAutSerializer, \
    GeocodeReliabilityAutSerializer, StateUserSerializer


class APIRoot(APIView):
    """
    Root api link
    """

    def get(self, request, format=None):
        return Response(
            {
                'users': reverse('user-list', request=request, format=format),
                'states': reverse('state-list', request=request, format=format)
            }
        )


class UserList(APIView):
    """
    List all user
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        user = User.objects.all()
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


'''
class StateList(APIView):
    """
    List all state, or create a new state
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        state = State.objects.all().prefetch_related('created_by').only('state_pid', 'date_created', 'date_retired', 'state_name', 'state_abbreviation', 'created_by__username')
        context = {'request': request}
        serializer = StateSerializer(state, many=True, context=context)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=self.request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StateDetail(APIView):
    """
    Retrieve, update or delete a state
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, state_pid):
        try:
            return State.objects.get(state_pid=state_pid)
        except State.DoesNotExist:
            raise Http404

    def get(self, request, state_pid, format=None):
        state = self.get_object(state_pid)
        context = {'request': request}
        serializer = StateSerializer(state, context=context)
        return Response(serializer.data)

    def put(self, request, state_pid, format=None):
        state = self.get_object(state_pid)
        serializer = StateSerializer(state, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, state_pid, format=None):
        state = self.get_object(state_pid)
        state.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
class StateViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'state_pid'


class LocalityViewSet(viewsets.ModelViewSet):
    """
    Locality view set with list, create, retrieve, update and destroy
    """
    queryset = Locality.objects.\
        select_related('state_pid').\
        select_related('locality_class_code').\
        select_related('gnaf_reliability_code').\
        only('locality_pid',
             'locality_name',
             'primary_postcode',
             'state_pid__state_name',
             'locality_class_code__name',
             'gnaf_reliability_code__name')
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



class StateUserViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = State.objects.raw('SELECT state_pid, state_name, username '
                                 'FROM state s '
                                 'LEFT JOIN auth_user au'
                                 '  ON s.created_by = au.id')

    serializer_class = StateUserSerializer
    permission_classes = [permissions.IsAuthenticated]
