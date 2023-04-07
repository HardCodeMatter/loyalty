from django.shortcuts import render, HttpResponse
from .models import Card
from .services import CardService
from typing import List


def card_list_view(request: HttpResponse) -> HttpResponse:
    service = CardService()
    cards: List[Card] = service.get_objects()

    context = {
        'cards': cards
    }

    return render(request, 'main/card_list.html', context)

def card_detail_view(request: HttpResponse, id: int) -> HttpResponse:
    service = CardService()
    card: Card = service.get_object_by_id(id)

    context = {
        'card': card
    }

    return render(request, 'main/card_detail.html', context)