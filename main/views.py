from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone
from .models import Card, CardHistory
from .services import CardService, CardHistoryService
from .forms import CardFormSet, CardHistoryForm
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

    if not card.is_expired and card.date_expired < timezone.now():
        card_service.update_object(id, is_expired=True, is_activated=False)

        return redirect(f'/card/{id}/')

    context = {
        'card': card,
        'histories': histories,
    }

    return render(request, 'main/card_detail.html', context)

def card_history_create_view(request: HttpResponse, id: int) -> HttpResponse:
    card_history_service = CardHistoryService()

    card_service = CardService()
    card: Card = card_service.get_object_by_id(id)

    if card.is_expired or not card.is_activated:
        return redirect(f'/card/{id}/')

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

def card_delete_view(request: HttpResponse, id: int) -> None:
    service = CardService()
    service.delete_object(id)

    return redirect(f'/card/')

def card_toggle_status_view(request: HttpResponse, id: int) -> HttpResponse:
    service = CardService()
    card: Card = service.get_object_by_id(id)

    if card.is_activated:
        service.update_object(id, is_activated=False)
    else:
        service.update_object(id, is_activated=True)

    return redirect(f'/card/{id}/')

def card_create_view(request: HttpResponse) -> HttpResponse:
    if request.method == 'POST':
        formset = CardFormSet(request.POST)
        
        if formset.is_valid():
            for form in formset:
                object = form.save(commit=False)
                object.number = form.cleaned_data['number']
                object.owner = form.cleaned_data['owner']
                object.balance = 0
                object.date_expired = form.cleaned_data['date_expired']
                object.is_activated = form.cleaned_data['is_activated']
                object.save()

            return redirect(f'/card/')
    else:
        formset = CardFormSet()

    context = {
        'formset': formset,
    }

    return render(request, 'main/card_create.html', context)
