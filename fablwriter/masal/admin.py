from django.contrib import admin
from masal.models import Fabl, Baglam, Sahne, Published

# Modelleri admin sayfasında yönetebilmek için kayıt ettik
admin.site.register(Fabl)
admin.site.register(Baglam)
admin.site.register(Sahne)
admin.site.register(Published)
