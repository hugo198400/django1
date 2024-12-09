from django import forms
from .models import RegAvance

class RegAvanceForm(forms.ModelForm):
    class Meta:
        model = RegAvance
        fields = ['id_punto', 'avance_km', 'avance_vol','estado']
        widgets = {
            'avance_km': forms.NumberInput(attrs={'steps':'0.01'}),
            'avance_vol': forms.NumberInput(attrs={'steps':'0.01'}),
        }