# Generated by Django 5.1.6 on 2025-04-10 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_infoextra_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='infoextra',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
    ]
