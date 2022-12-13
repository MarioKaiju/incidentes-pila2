# Generated by Django 4.0 on 2022-12-13 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0001_initial'),
        ('incidentes', '0003_incidente_fecha'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incidente',
            old_name='id_vehiculo',
            new_name='id_incidente',
        ),
        migrations.AlterField(
            model_name='incidente',
            name='modelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculos.vehiculo'),
        ),
    ]
