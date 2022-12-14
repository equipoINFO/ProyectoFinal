# Generated by Django 4.1 on 2022-08-23 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('contenido', models.TextField()),
                ('img', models.ImageField(blank=True, help_text='seleccione una imagen para mostrar', null=True, upload_to='img/noticias')),
                ('creado', models.DateTimeField(default=django.utils.timezone.now)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('pubicado', models.DateTimeField(blank=True, null=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(related_name='noticias', to='noticias_app.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuerpo_comentario', models.TextField()),
                ('creado', models.DateTimeField(default=django.utils.timezone.now)),
                ('aprobado', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='noticias_app.noticia')),
            ],
        ),
    ]
