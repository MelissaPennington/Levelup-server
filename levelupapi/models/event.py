from django.db import models
from .gamer import Gamer
from .game import Game

class Event(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='events')
    description = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    organizer = models.ForeignKey(Gamer, on_delete=models.CASCADE, related_name='user_event')
    objects = models.Manager()
