# Generated by Django 5.1.6 on 2025-04-09 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_rename_ifoextra_infoextra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infoextra',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes'),
        ),
    ]
