from django.urls import path
from . import views


urlpatterns = [
    path('', views.card_list_view, name='card_list'),
]
