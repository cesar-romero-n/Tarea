# Generated by Django 4.2.2 on 2023-06-29 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_alter_productosminimos_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productosminimos',
            name='fecha_de_registro',
            field=models.CharField(max_length=8, verbose_name='Fecha de registro'),
        ),
    ]
