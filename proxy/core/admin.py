from django.contrib import admin

# Register your models here.
from .models import Pacote, Adquirente

admin.site.register(Pacote)
admin.site.register(Adquirente)
