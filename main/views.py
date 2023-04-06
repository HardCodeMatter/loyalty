from django.shortcuts import render
from .services import CardService


def card_list_view(request):
    service = CardService()
    cards = service.get_objects()

    context = {
        'cards': cards
    }

    return render(request, 'main/card_list.html', context)