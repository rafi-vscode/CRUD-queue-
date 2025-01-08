from django import forms
from .models import Antrian

class AntrianForm(forms.ModelForm):
    class Meta:
        model = Antrian
        fields = ['nama', 'umur', 'nomor_hp', 'poli']
