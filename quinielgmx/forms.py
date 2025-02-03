from django import forms
from .models import Prediccion

class PrediccionForm(forms.ModelForm):
    class Meta:
        model = Prediccion
        fields = ['goles_local_pred', 'goles_visitante_pred']