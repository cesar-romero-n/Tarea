from django.contrib import admin
from .models import ProductosMinimos   #Estamos importando en admin el modelo (Tabla) de ProductosMinimos

admin.site.register(ProductosMinimos) #Importación de ProductosMinimos de models.py