from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from django.http import Http404

from places.models import State
from places.serializers import StateSerializer


class StateList(APIView):
    """
    List all state, or create a new state
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        state = State.objects.all()
        serializer = StateSerializer(state, many=True)
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
        serializer = StateSerializer(state)
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
