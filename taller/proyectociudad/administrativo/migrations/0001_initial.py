# Generated by Django 3.2.4 on 2021-06-26 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('ciudad', models.CharField(max_length=30)),
                ('tipo_edificio', models.CharField(choices=[('residencial', 'Tipo residencial'), ('comercial', 'Tipo comercial')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_prop', models.CharField(max_length=100)),
                ('costo_depart', models.DecimalField(decimal_places=2, max_digits=100)),
                ('numero_cuartos', models.IntegerField()),
                ('edificio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='edificios', to='administrativo.edificio')),
            ],
        ),
    ]
