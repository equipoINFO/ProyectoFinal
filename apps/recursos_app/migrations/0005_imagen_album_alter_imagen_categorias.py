# Generated by Django 4.1 on 2022-08-30 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos_app', '0004_alter_imagen_categorias'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagen',
            name='album',
            field=models.ManyToManyField(related_name='álbumdefotos', to='recursos_app.albumfotos'),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='categorias',
            field=models.ManyToManyField(related_name='imágenes', to='recursos_app.categoria'),
        ),
    ]
