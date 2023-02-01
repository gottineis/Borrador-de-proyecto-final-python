# Generated by Django 4.1.4 on 2023-01-17 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppHospitalV', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad', models.CharField(max_length=50)),
                ('adulto', models.IntegerField()),
                ('pediatrico', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estudio', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=30)),
                ('sangre', models.BooleanField()),
                ('orina', models.BooleanField()),
                ('otro', models.BooleanField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Profesor',
            new_name='Staff',
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
    ]
