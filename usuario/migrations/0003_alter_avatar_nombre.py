# Generated by Django 3.2.6 on 2021-08-31 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_alter_avatar_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]