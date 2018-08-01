from random import choice
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import FablForm
from masal.models import Baglam, Fabl, Sahne

def home(request):
    fables = Fabl.objects.all()
    return render(request, 'home.html', {
        'title': 'FABLOPİCASSO',
        'fables': fables,
    })

def fabl_create(request):
    form = FablForm()
    if request.method == 'POST':
        form = FablForm(request.POST)
        if form.is_valid():
            baslik = Fabl.objects.create(baslik=form.cleaned_data['baslik'],
                user=request.user,
            )
            Sahne.objects.create(
                anahtar='B',
                deger=form.cleaned_data['baslik'],
                secenek='I',
                fabl_id=baslik,
            )
            girizgah = Sahne.objects.create(
                anahtar='G',
                deger=form.cleaned_data['girizgah'],
                secenek='I',
                fabl_id=baslik,
            )
            serim = Sahne.objects.create(
                anahtar='S',
                deger=form.cleaned_data['serim'],
                secenek='I',
                fabl_id=baslik,
            )
            dugum = Sahne.objects.create(
                anahtar='D',
                deger=form.cleaned_data['dugum'],
                secenek='I',
                fabl_id=baslik,
            )
            cozum = Sahne.objects.create(
                anahtar='C',
                deger=form.cleaned_data['cozum'],
                secenek=form.cleaned_data['cozum_secenek'],
                fabl_id=baslik,
            )
            return redirect(reverse("publish", args=[baslik.id]))
    return render(request, 'fabl_create.html', {
        'title': 'FABLE-CREATE',
        'form': form,
    })

def fabl_publish(request, id):
    id = Fabl.objects.get(id=id)
    sahnes = Sahne.objects.filter(fabl_id=id)
    return render(request, 'fabl_publish.html', {
        'fabl': id,
        'sahnes': sahnes,
    })

def about(request):
        return render(request, 'about.html')

def login(request):
        return render(request, 'login.html')

def profile(request):
        return render(request, 'profile.html')

def signup(request):
        return render(request, 'signup.html')
