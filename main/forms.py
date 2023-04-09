from django import forms
from .models import Card, CardHistory


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('number', 'owner', 'date_expired', 'is_activated',)


CardFormSet = forms.formset_factory(CardForm, extra=3)


class CardHistoryForm(forms.ModelForm):
    class Meta:
        model = CardHistory
        fields = ('label', 'bonus',)
