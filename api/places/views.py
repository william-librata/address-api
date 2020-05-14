from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import generics

from django.http import Http404

from django.contrib.auth.models import User

from places.models import State
from places.serializers import StateSerializer, UserSerializer


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


class StateList(APIView):
    """
    List all state, or create a new state
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        state = State.objects.all()
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

    def get_object(self, state_abbreviation):
        try:
            return State.objects.get(state_abbreviation=state_abbreviation)
        except State.DoesNotExist:
            raise Http404

    def get(self, request, state_abbreviation, format=None):
        state = self.get_object(state_abbreviation)
        context = {'request': request}
        serializer = StateSerializer(state, context=context)
        return Response(serializer.data)

    def put(self, request, state_abbreviation, format=None):
        state = self.get_object(state_abbreviation)
        serializer = StateSerializer(state, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, state_abbreviation, format=None):
        state = self.get_object(state_abbreviation)
        state.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


