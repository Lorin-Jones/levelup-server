from django.db import models

from levelupapi.models.gamer import Gamer


class EventGamer(models.Model):

    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name = "eventgamers")
    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name="eventgamers")