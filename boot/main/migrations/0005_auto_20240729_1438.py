# Generated by Django 3.2.25 on 2024-07-29 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20240729_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='aprobado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='materia',
            name='regular',
            field=models.BooleanField(default=True),
        ),
    ]
