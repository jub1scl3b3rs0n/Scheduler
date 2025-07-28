from django import forms
import json
from .models import ServiceProvider

DAYS_OF_WEEK = [
    ("monday", "Segunda"),
    ("tuesday", "Terça"),
    ("wednesday", "Quarta"),
    ("thursday", "Quinta"),
    ("friday", "Sexta"),
    ("saturday", "Sábado"),
    ("sunday", "Domingo"),
]

class AvailabilityForm(forms.Form):
    for day, label in DAYS_OF_WEEK:
        locals()[day] = forms.CharField(
            required=False,
            label=label,
            widget=forms.TextInput(attrs={"placeholder": "Ex: 09:00,14:30"})
        )
