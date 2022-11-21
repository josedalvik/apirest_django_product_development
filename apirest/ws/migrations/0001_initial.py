# Generated by Django 4.1.3 on 2022-11-21 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prediccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('alpha', models.DecimalField(decimal_places=23, max_digits=30)),
                ('delta', models.DecimalField(decimal_places=23, max_digits=30)),
                ('u', models.DecimalField(decimal_places=23, max_digits=30)),
                ('g', models.DecimalField(decimal_places=23, max_digits=30)),
                ('r', models.DecimalField(decimal_places=23, max_digits=30)),
                ('i', models.DecimalField(decimal_places=23, max_digits=30)),
                ('z', models.DecimalField(decimal_places=23, max_digits=30)),
                ('redshift', models.DecimalField(decimal_places=23, max_digits=30)),
                ('fecha_creacion', models.DateField(blank=True, default=None, null=True)),
                ('galaxy', models.DecimalField(blank=True, decimal_places=23, default=None, max_digits=30, null=True)),
                ('qso', models.DecimalField(blank=True, decimal_places=23, default=None, max_digits=30, null=True)),
                ('star', models.DecimalField(blank=True, decimal_places=23, default=None, max_digits=30, null=True)),
                ('valor_real', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('fecha_actualizacion', models.DateField(blank=True, default=None, null=True)),
            ],
        ),
    ]
