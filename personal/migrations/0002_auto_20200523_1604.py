# Generated by Django 3.0.4 on 2020-05-23 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='per_documento',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='personal.Persona'),
        ),
    ]