from django.shortcuts import render


def card_list_view(request):

    context = {}

    return render(request, 'main/card_list.html', context)