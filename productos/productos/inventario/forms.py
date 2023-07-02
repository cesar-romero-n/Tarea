from django import forms
from .models import ProductosMinimos

class ProductoForm(forms.ModelForm):
    class Meta:
        model = ProductosMinimos
        fields = ['nombre', 'descripcion', 'precio', 'fecha_de_registro', 'estatus']

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        descripcion = cleaned_data.get('descripcion')
        precio = cleaned_data.get('precio')
        fecha_de_registro = cleaned_data['fecha_de_registro']
        estatus = cleaned_data['estatus']

        if not nombre or not descripcion or not precio or not fecha_de_registro: #No se incluye estatus, para permitir un cero
            raise forms.ValidationError('Todos los campos deben estar completos')
        
        return cleaned_data