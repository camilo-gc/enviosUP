# Generated by Django 3.0.4 on 2020-03-28 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_vehiculo',
            fields=[
                ('tv_id', models.AutoField(primary_key=True, serialize=False)),
                ('tv_nombre', models.CharField(max_length=100)),
                ('tv_descripcion', models.CharField(blank=True, max_length=350, null=True)),
                ('tv_estado', models.IntegerField(default=1, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('veh_id', models.AutoField(primary_key=True, serialize=False)),
                ('veh_marca', models.CharField(max_length=50)),
                ('veh_modelo', models.CharField(max_length=50)),
                ('veh_matricula', models.CharField(max_length=50)),
                ('veh_capacidad', models.CharField(max_length=50)),
                ('veh_cubicaje', models.CharField(max_length=50)),
                ('veh_estado', models.IntegerField(default=1, max_length=1)),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='personal.Empleado')),
                ('tv_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vehiculo.Tipo_vehiculo')),
            ],
        ),
    ]
