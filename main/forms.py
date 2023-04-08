from django import forms
from .models import CardHistory


class CardHistoryForm(forms.ModelForm):
    class Meta:
        model = CardHistory
        fields = ('label', 'bonus',)
