# Generated by Django 4.1.3 on 2022-12-16 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_configuracion_construido_por'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='subtitulo_principal',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='configuracion',
            name='titulo_principal',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='construido_por',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='nombre_blog',
            field=models.CharField(default='', max_length=14),
        ),
    ]
