# Generated by Django 3.0.4 on 2020-05-23 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mercancia',
            name='mer_contenido',
            field=models.CharField(max_length=350, null=True),
        ),
    ]
