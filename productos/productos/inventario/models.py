from django.db import models

# Create your models here.
class ProductosMinimos(models.Model):

    class Meta:
        verbose_name = 'ProductosMinimos'
        verbose_name_plural = 'ProductosMinimos' #Se cambia el plural para mostrar sólo una S en SQL

    nombre = models.CharField('Nombre', max_length=300, blank=False, default='Nombre del producto')
    descripcion = models.CharField('Descripción', max_length=300, default='Sin descripción')
    precio = models.DecimalField('Precio',max_digits=10,decimal_places=2,blank=False, default=000.00)
    fecha_de_registro = models.CharField('Fecha de registro',max_length=8, blank=False,default='mm/dd/yy') #Fecha en formato mes/día/año
    estatus = models.BooleanField('Estatus', default=True) #Se deja el valor como True, para mostrar palomeado el campo

    def __str__(self):
        return self.nombre