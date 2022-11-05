"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event, Gamer, Game


class EventView(ViewSet):
    """Level up game types view"""

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        organizer = Gamer.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.data["game"])

        event = Event.objects.create(
            game=game,
            description=request.data["description"],
            date=request.data["date"],
            time=request.data["time"],
            organizer=organizer,
        )
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def list(self, request):
        event = Event.objects.all()

        if "game" in request.query_params:
            event = event.filter(game = request.query_params['game'])
        
        serializer = EventSerializer(event, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

class EventGamerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gamer
        fields = ('user', 'bio', )        

class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    gamers = EventGamerSerializer(many=True)

    class Meta:
        model = Event
        fields = ('id', 'game', 'description', 'date', 'time', 'organizer', 'gamers', )