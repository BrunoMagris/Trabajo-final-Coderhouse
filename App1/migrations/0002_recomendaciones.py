# Generated by Django 4.1 on 2022-10-18 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recomendaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=60)),
                ('Localizacion', models.CharField(max_length=60)),
                ('Categoria', models.CharField(max_length=60)),
                ('Especialidad', models.CharField(max_length=60)),
                ('Reseña', models.CharField(max_length=200)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='recomendaciones')),
            ],
        ),
    ]
