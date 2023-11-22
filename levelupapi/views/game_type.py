"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import GameType


class GameTypeView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
            # Retrieve a single GameType from the database based on the pk
        game_type = GameType.objects.get(pk=pk)

            # Serialize the retrieved GameType
        serializer = GameTypeSerializer(game_type)

            # Return the serialized data as a JSON response
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
            # Retrieve a single GameType from the database based on the pk
        game_types = GameType.objects.all()

            # Serialize the retrieved GameType
        serializer = GameTypeSerializer(game_types, many=True)

            # Return the serialized data as a JSON response
        return Response(serializer.data)


class GameTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = GameType
        fields = ('id', 'label')
