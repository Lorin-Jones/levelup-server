
from django.db import models

class Event(models.Model):

    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name='events')
    description = models.CharField(max_length=1000)
    date = models.DateField()
    time = models.TimeField()
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='event_organizer')
    gamers = models.ManyToManyField("Gamer", through = "EventGamer")