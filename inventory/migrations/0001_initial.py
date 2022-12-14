# Generated by Django 4.1.2 on 2022-10-04 22:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=50, verbose_name='Referencia')),
                ('brand', models.CharField(max_length=50, verbose_name='Marca')),
                ('processor', models.CharField(max_length=50, verbose_name='Procesador')),
                ('memory', models.CharField(max_length=50, verbose_name='Memoria')),
                ('disk', models.CharField(max_length=50, verbose_name='Disco')),
                ('type', models.CharField(max_length=50, verbose_name='Tipo')),
            ],
        ),
        migrations.CreateModel(
            name='UserEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_assignment', models.DateTimeField(max_length=50, verbose_name='Fecha de asignación')),
                ('date_delivery', models.DateTimeField(max_length=50, verbose_name='Fecha de entrega')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.equipment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
