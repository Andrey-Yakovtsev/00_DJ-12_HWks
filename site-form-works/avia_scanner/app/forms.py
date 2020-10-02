from django import forms

from .widgets import AjaxInputWidget
from .models import City


class SearchTicket(forms.Form):
    from_city = forms.ModelChoiceField(queryset=City.objects.all())
    to_city = forms.ModelChoiceField(queryset=City.objects.all())
    date = forms.DateTimeField
