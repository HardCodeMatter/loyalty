from django.db import models
from django.utils import timezone


class Card(models.Model):
    number = models.IntegerField(('number'), unique=True, blank=True)
    owner = models.CharField(('owner'), max_length=100)
    date_released = models.DateTimeField(('date released'), default=timezone.now)
    date_expired = models.DateTimeField(('date expired'))
    balance = models.FloatField(('balance'))
    
    is_activated = models.BooleanField(('activated'), default=False)
    is_expired = models.BooleanField(('expired'), default=False)

    def __str__(self):
        return f'Card {self.pk}'
