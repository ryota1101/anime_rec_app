# Generated by Django 3.2.19 on 2023-06-22 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studio',
            name='en_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='studio',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
