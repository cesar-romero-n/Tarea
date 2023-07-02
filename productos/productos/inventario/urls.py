from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos', views.Productos.as_view(), name='productos'),
    path('formulario', views.Formulario.as_view(), name='formulario'), #Se crean dos htmls, para separar el formulario de la consulta
]