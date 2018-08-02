from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SahneForm, BaglamFormset
from masal.models import Baglam, Fabl, Sahne, Published

def home(request):
    fables = Published.objects.all()
    return render(request, 'home.html', {
        'title': 'FABLOPICASSO',
        'fables': fables,
    })

def fabl_create(request):
    sahne_form = SahneForm()
    baglam_formset = BaglamFormset()
    baglamlist = []
    basliklist = []
    girizgahlist = []
    serimlist = []
    dugumlist = []
    cozumlist = []

    if request.method == 'POST':
        sahne_form = SahneForm(request.POST)
        baglam_formset = BaglamFormset(request.POST)
        if sahne_form.is_valid() and baglam_formset.is_valid():
            baslik = sahne_form.cleaned_data['baslik']
            girizgah = sahne_form.cleaned_data['girizgah']
            serim = sahne_form.cleaned_data['serim']
            dugum = sahne_form.cleaned_data['dugum']
            cozum = sahne_form.cleaned_data['cozum']

            for form in baglam_formset:
                baglamlist.append((form.cleaned_data.get('anahtar'),
                    form.cleaned_data.get('deger'),
                    form.cleaned_data.get('extra'),
                ))

            # Variable exchange with deger
            for baglam in baglamlist:
                for word in baslik.split():
                    if word.lower().startswith(baglam[1].lower()):
                        word = word.lower().replace(baglam[1].lower(), "{"+baglam[0].lower()+"}")
                    basliklist.append(word)
                baslik = " ".join(basliklist)
                basliklist = []

                for word in girizgah.split():
                    if word.lower().startswith(baglam[1].lower()):
                        word = word.lower().replace(baglam[1].lower(), "{"+baglam[0].lower()+"}")
                    girizgahlist.append(word)
                girizgah = " ".join(girizgahlist)
                girizgahlist = []

                for word in serim.split():
                    if word.lower().startswith(baglam[1].lower()):
                        word = word.lower().replace(baglam[1].lower(), "{"+baglam[0].lower()+"}")
                    serimlist.append(word)
                serim = " ".join(serimlist)
                serimlist = []

                for word in dugum.split():
                    if word.lower().startswith(baglam[1].lower()):
                        word = word.lower().replace(baglam[1].lower(), "{"+baglam[0].lower()+"}")
                    dugumlist.append(word)
                dugum = " ".join(dugumlist)
                dugumlist = []

                for word in cozum.split():
                    if word.lower().startswith(baglam[1].lower()):
                        word = word.lower().replace(baglam[1].lower(), "{"+baglam[0].lower()+"}")
                    cozumlist.append(word)
                cozum = " ".join(cozumlist)
                cozumlist = []

            tempbaslik = baslik
            baslik = Fabl.objects.create(baslik=baslik, user=request.user)
            Sahne.objects.create(anahtar='B', deger=baslik, secenek='I', fabl_id=baslik)
            Sahne.objects.create(anahtar='G', deger=girizgah, secenek='I', fabl_id=baslik)
            Sahne.objects.create(anahtar='S', deger=serim, secenek='I', fabl_id=baslik)
            Sahne.objects.create(anahtar='D', deger=dugum, secenek='I', fabl_id=baslik)
            Sahne.objects.create(
                anahtar='C',
                deger=cozum,
                secenek=sahne_form.cleaned_data['cozum_secenek'],
                fabl_id=baslik,
            )

            for baglam in baglamlist:
                tempbaslik = tempbaslik.replace("{"+baglam[0]+"}", baglam[2])
                girizgah = girizgah.replace("{"+baglam[0]+"}", baglam[2])
                serim = serim.replace("{"+baglam[0]+"}", baglam[2])
                dugum = dugum.replace("{"+baglam[0]+"}", baglam[2])
                cozum = cozum.replace("{"+baglam[0]+"}", baglam[2])

            published = Published.objects.create(
                title=tempbaslik,
                content=girizgah+" "+serim+" "+dugum+" "+cozum,
                user=request.user,
            )

            for form in baglam_formset:
                anahtar = form.cleaned_data.get('anahtar')
                deger = form.cleaned_data.get('deger')
                if anahtar and deger:
                    Baglam(anahtar=anahtar, deger=deger, fabl_id=baslik).save()
            return redirect(reverse("publish", args=[published.id]))
    return render(request, 'fabl_create.html', {
        'title': 'FABLE-CREATE',
        'sahne_form': sahne_form,
        'baglam_formset': baglam_formset,
    })

def fabl_publish(request, id):
    id = Published.objects.get(id=id)
    return render(request, 'fabl_publish.html', {
        'fabl': id,
    })
