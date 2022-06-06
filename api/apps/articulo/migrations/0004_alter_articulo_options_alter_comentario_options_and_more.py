# Generated by Django 4.0.4 on 2022-06-06 00:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articulo', '0003_articulo_creado'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articulo',
            options={'verbose_name_plural': 'Articulos'},
        ),
        migrations.AlterModelOptions(
            name='comentario',
            options={'verbose_name_plural': 'Comentarios'},
        ),
        migrations.AlterModelOptions(
            name='imagenes',
            options={'verbose_name_plural': 'Imagenes'},
        ),
        migrations.AddField(
            model_name='comentario',
            name='creado',
            field=models.DateTimeField(auto_now_add=True, default=None, help_text='Fecha de creacion', verbose_name='creado'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comentario',
            name='modificado',
            field=models.DateTimeField(auto_now=True, help_text='Fecha de modificaion', verbose_name='modificado'),
        ),
        migrations.AlterModelTable(
            name='articulo',
            table='articulo_Articulo',
        ),
        migrations.AlterModelTable(
            name='comentario',
            table='articulo_comentario',
        ),
        migrations.AlterModelTable(
            name='imagenes',
            table='articulo_imagenes',
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True, help_text='Fecha de creacion', verbose_name='creado')),
                ('modificado', models.DateTimeField(auto_now=True, help_text='Fecha de modificaion', verbose_name='modificado')),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articulo.articulo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Likes',
                'db_table': 'articulo_like',
            },
        ),
    ]
