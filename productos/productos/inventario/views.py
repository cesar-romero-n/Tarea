from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
import json

from .models import ProductosMinimos
from .forms import ProductoForm


def index(request):
    
    return HttpResponse("Hola mundo")

class Productos(View): #Clase Productos con Get, ya que no introduciremos información para enviar a la base de datos
    template_name = 'productos.html'

 
    def get(self, request):
        productosminimos = ProductosMinimos.objects.all()
        form = ProductoForm()
        return render(request, self.template_name, {'form': form, 'productosminimos': productosminimos})

class Formulario(View): #Clase Formulario con Post y Get, para enviar información a la BD
    template_name = 'formulario.html'
    
    def post(self, request):
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formulario')

        return render(request, self.template_name, {'form': form})
    
    def get(self, request):
        productosminimos = ProductosMinimos.objects.all()
        form = ProductoForm()
        return render(request, self.template_name, {'form': form, 'productosminimos': productosminimos})
