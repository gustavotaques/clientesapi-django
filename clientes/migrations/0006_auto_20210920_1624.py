# Generated by Django 3.0.8 on 2021-09-20 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20210916_1214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='primeiro_nome',
            new_name='nome',
        ),
    ]
