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

    def __str__(self) -> str:
        return f'Card {self.pk}'
    
    class Meta:
        verbose_name = 'card'
        verbose_name_plural = 'cards'


class CardHistory(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    label = models.CharField(('label'), max_length=100)
    bonus = models.FloatField(('bonus'))
    balance = models.FloatField(('balance'))
    date_used = models.DateTimeField(('date used'), default=timezone.now)

    def __str__(self) -> str:
        return f'Card {self.card}'

    class Meta:
        verbose_name = 'card history'
        verbose_name_plural = 'card histories'
