# Generated by Django 4.1 on 2022-09-10 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLavatres', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='fecha_turno',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='indumentaria',
            name='fecha_retiro',
            field=models.DateTimeField(),
        ),
    ]
