from django.db import models

class Fabl(models.Model):
    baslik = models.CharField(max_length=100)
    yazar = models.CharField(max_length=100)
    tarih = models.DateField()

    def __str__(self):
        return self.baslik

class Baglam(models.Model):
    anahtar = models.CharField(max_length=100)
    deger = models.CharField(max_length=100)

    def __str__(self):
        return self.anahtar+" -- "+self.deger

class Sahne(models.Model):
    SAHNE_TIPLERI = (
        ('G', 'Girizgah'),
        ('S', 'Serim'),
        ('D', 'Düğüm'),
        ('C', 'Çözüm'),
        ('O', 'Öğüt'),
    )
    SECENEK = (
        ('I', 'İyi'),
        ('K', 'Kötü'),
    )
    anahtar = models.CharField(max_length=1, choices=SAHNE_TIPLERI)
    deger = models.TextField()
    secenek = models.CharField(max_length=1, choices=SECENEK)
    fabl_id = models.ForeignKey(Fabl, on_delete=models.CASCADE)

    def __str__(self):
        return self.anahtar+" -- "+self.secenek