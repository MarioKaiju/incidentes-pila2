# Generated by Django 4.0 on 2022-12-13 02:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('incidentes', '0004_rename_id_vehiculo_incidente_id_incidente_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UUIDModel',
            fields=[
                ('id_incidente', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='incidente',
            name='id_incidente',
        ),
        migrations.AddField(
            model_name='incidente',
            name='uuidmodel_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='incidentes.uuidmodel'),
            preserve_default=False,
        ),
    ]