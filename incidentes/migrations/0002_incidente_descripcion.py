# Generated by Django 4.0 on 2022-12-13 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidentes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidente',
            name='descripcion',
            field=models.TextField(),
            preserve_default=False,
        ),
    ]
