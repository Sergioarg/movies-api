# Generated by Django 5.0.6 on 2024-06-01 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20240601_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='original_lang',
            field=models.CharField(help_text='Enter a original language (e.g. en)', max_length=10),
        ),
    ]
