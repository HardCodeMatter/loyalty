from django.contrib import admin
from .models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('number', 'owner', 'date_released', 'date_expired', 'balance',)
    list_filter = ('number', 'owner', 'date_released', 'date_expired', 'balance',)

    fieldsets = [
        (None, {
            'fields': ('number', 'owner', 'balance',),
        }),
        ('Date and time', {
            'fields': ('date_released', 'date_expired',),
        }),
        ('Card status', {
            'fields': ('is_activated', 'is_expired',),
        }),
    ]

    search_fields = ('number', 'owner', 'date_released', 'date_expired', 'balance',)
    ordering = ('-id',)
