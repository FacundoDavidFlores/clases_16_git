# Generated by Django 4.1.3 on 2022-12-08 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='familiar',
            old_name='numero_pasaport',
            new_name='numero_pasaporte',
        ),
    ]
