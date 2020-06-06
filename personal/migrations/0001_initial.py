# Generated by Django 3.0.4 on 2020-05-25 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionalidad',
            fields=[
                ('fun_id', models.AutoField(primary_key=True, serialize=False)),
                ('fun_nombre', models.CharField(max_length=100)),
                ('fun_descripcion', models.CharField(blank=True, max_length=350, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('rol_id', models.AutoField(primary_key=True, serialize=False)),
                ('rol_nombre', models.CharField(max_length=50)),
                ('rol_descripcion', models.CharField(blank=True, max_length=350, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_documento',
            fields=[
                ('td_id', models.AutoField(primary_key=True, serialize=False)),
                ('td_nombre', models.CharField(max_length=50)),
                ('td_descripcion', models.CharField(blank=True, max_length=350, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('per_documento', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('per_nombre', models.CharField(max_length=50)),
                ('per_apellido', models.CharField(max_length=50)),
                ('per_fecha_naci', models.DateField(null=True)),
                ('per_email', models.EmailField(max_length=254, null=True)),
                ('per_contrasena', models.CharField(max_length=512)),
                ('per_telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('per_celular', models.CharField(blank=True, max_length=10, null=True)),
                ('per_direccion', models.CharField(max_length=100)),
                ('td_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='personal.Tipo_documento')),
            ],
        ),
        migrations.CreateModel(
            name='Funcionalidad_rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fun_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='personal.Funcionalidad')),
                ('rol_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='personal.Rol')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('emp_inicio_contrato', models.DateField()),
                ('emp_fin_contrato', models.DateField()),
                ('emp_salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('emp_estado', models.IntegerField(default=1, max_length=1)),
                ('per_documento', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='personal.Persona')),
                ('rol_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='personal.Rol')),
                ('suc_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empresa.Sucursal')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cli_id', models.AutoField(primary_key=True, serialize=False)),
                ('cli_estado', models.IntegerField(default=1, max_length=1)),
                ('cli_fecha_registro', models.DateField()),
                ('per_documento', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='personal.Persona')),
            ],
        ),
    ]
