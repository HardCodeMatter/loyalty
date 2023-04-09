from django.urls import path
from django.shortcuts import redirect
from . import views


urlpatterns = [
    path('', lambda req: redirect('card/')),
    path('create/', views.card_create_view, name='card_create'),
    path('card/', views.card_list_view, name='card_list'),
    path('card/<int:id>/', views.card_detail_view, name='card_detail'),
    path('card/<int:id>/create/', views.card_history_create_view, name='card_history_create'),
    path('card/<int:id>/update/', views.card_toggle_status_view, name='card_toggle_status'),
    path('card/<int:id>/delete/', views.card_delete_view, name='card_delete'),
]
