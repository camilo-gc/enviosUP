# Generated by Django 3.0.4 on 2020-04-13 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_persona_per_contrasena'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='per_contrasena',
            field=models.CharField(max_length=512),
        ),
    ]
