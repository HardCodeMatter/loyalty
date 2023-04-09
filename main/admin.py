from django.contrib import admin
from .models import Card, CardHistory


class CardHistoryInline(admin.StackedInline):
    model = CardHistory
    extra = 0


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('number', 'owner', 'date_released', 'date_expired', 'balance', 'is_activated', 'is_expired',)
    list_filter = ('number', 'owner', 'date_released', 'date_expired', 'balance', 'is_activated', 'is_expired',)

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

    search_fields = ('number', 'owner', 'date_released', 'date_expired', 'balance', 'is_activated', 'is_expired',)
    ordering = ('-id',)
    inlines = (CardHistoryInline,)


@admin.register(CardHistory)
class CardHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'card', 'label', 'bonus', 'balance', 'date_used',)
    list_filter = ('id', 'card', 'label', 'bonus', 'balance', 'date_used',)

    fieldsets = [
        (None, {
            'fields': ('card', 'label',),
        }),
        ('Date and time', {
            'fields': ('date_used',),
        }),
        ('Card balance', {
            'fields': ('bonus', 'balance',),
        }),
    ]

    search_fields = ('id', 'card', 'label', 'bonus', 'balance', 'date_used',)
    ordering = ('-id',)
