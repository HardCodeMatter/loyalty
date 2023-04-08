from django.shortcuts import render, redirect, HttpResponse
from .models import Card, CardHistory
from .services import CardService, CardHistoryService
from .forms import CardHistoryForm
from typing import List


def card_list_view(request: HttpResponse) -> HttpResponse:
    service = CardService()
    cards: List[Card] = service.get_objects()

    context = {
        'cards': cards
    }

    return render(request, 'main/card_list.html', context)

def card_detail_view(request: HttpResponse, id: int) -> HttpResponse:
    card_service = CardService()
    card: Card = card_service.get_object_by_id(id)

    card_history_service = CardHistoryService()
    histories: List[CardHistory] = card_history_service.filter_object_by_id(card.pk)

    context = {
        'card': card,
        'histories': histories,
    }

    return render(request, 'main/card_detail.html', context)

def card_history_create_view(request: HttpResponse, id: int) -> HttpResponse:
    card_history_service = CardHistoryService()

    card_service = CardService()
    card: Card = card_service.get_object_by_id(id)

    if request.method == 'POST':
        form = CardHistoryForm(request.POST)

        if form.is_valid():
            card_history_service.create_object(
                card = card,
                label = form.cleaned_data['label'],
                bonus = form.cleaned_data['bonus'],
                balance = card.balance + form.cleaned_data['bonus']
            )

            card_service.update_object(
                id, 
                balance = card.balance + form.cleaned_data['bonus']
            )
            
            return redirect(f'/card/{id}/')
    else:
        form = CardHistoryForm()

    context = {
        'form': form,
    }

    return render(request, 'main/card_history_create.html', context)
