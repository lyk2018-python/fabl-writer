from django import forms
from django.forms import formset_factory

from .models import SECENEK

class SahneForm(forms.Form):
    baslik = forms.CharField(label='Başlık', max_length=100)
    girizgah = forms.CharField(label='Girizgah', widget=forms.Textarea)
    serim = forms.CharField(label='Serim', widget=forms.Textarea)
    dugum = forms.CharField(label='Düğüm', widget=forms.Textarea)
    cozum = forms.CharField(label='Çözüm', widget=forms.Textarea)
    cozum_secenek = forms.ChoiceField(choices=SECENEK)

class BaglamForm(forms.Form):
    anahtar = forms.CharField(
        label='Anahtar',
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter variable'
        })
    )
    deger = forms.CharField(
        label='First',
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter first value'
        })
    )
    extra = forms.CharField(
        label='Last',
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter last value'
        })
    )
BaglamFormset = formset_factory(BaglamForm, extra=3)
