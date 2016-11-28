from django import forms

# from .models import Account
from .models import Historique

class HistoriqueForm(forms.ModelForm):

    class Meta:
        model = Historique
        fields = ('content',)