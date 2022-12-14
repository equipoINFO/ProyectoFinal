# Generated by Django 4.1 on 2022-08-30 20:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('contenido', models.TextField()),
                ('img', models.ImageField(blank=True, help_text='Seleccione una imagen para mostrar', null=True, upload_to='img/noticias')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('publicado', models.DateTimeField(blank=True, null=True)),
                ('modalidad', models.TextField()),
                ('lugar', models.TextField()),
                ('precio', models.CharField(max_length=50)),
                ('categorias', models.ManyToManyField(related_name='eventos', to='eventos_app.categoria')),
            ],
        ),
    ]
