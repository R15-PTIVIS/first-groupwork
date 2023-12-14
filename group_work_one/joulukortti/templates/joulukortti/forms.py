from django import forms

from joulukortti.models import Color


class AddColorToPaletteForm(forms.Form):
    available_colors = forms.ModelMultipleChoiceField(
        queryset=Color.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )