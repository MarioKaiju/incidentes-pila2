# Generated by Django 4.0 on 2022-12-13 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidentes', '0002_incidente_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidente',
            name='fecha',
            field=models.DateTimeField(),
            preserve_default=False,
        ),
    ]