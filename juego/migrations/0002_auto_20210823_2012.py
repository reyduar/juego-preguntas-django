# Generated by Django 3.2.6 on 2021-08-23 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nivel',
            options={'ordering': ['nombre'], 'verbose_name': 'nivele'},
        ),
        migrations.AlterModelOptions(
            name='opcion',
            options={'ordering': ['opcion'], 'verbose_name': 'opcione'},
        ),
    ]