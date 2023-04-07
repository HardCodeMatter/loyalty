from django.urls import path
from django.shortcuts import redirect
from . import views


urlpatterns = [
    path('', lambda req: redirect('card/')),
    path('card/', views.card_list_view, name='card_list'),
    path('card/<int:id>/', views.card_detail_view, name='card_detail'),
]
