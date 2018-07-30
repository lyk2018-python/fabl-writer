from django import forms
from .models import SECENEK

class FablForm(forms.Form):
    baslik = forms.CharField(label='Başlık', max_length=100)
    girizgah = forms.CharField(label='Girizgah', widget=forms.Textarea)
    serim = forms.CharField(label='Serim', widget=forms.Textarea)
    dugum = forms.CharField(label='Düğüm', widget=forms.Textarea)
    cozum = forms.CharField(label='Çözüm', widget=forms.Textarea)
    cozum_secenek = forms.ChoiceField(choices=SECENEK)
