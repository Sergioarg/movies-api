# Generated by Django 5.0.6 on 2024-06-02 03:06

import django.core.validators
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_original_lang'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.DecimalField(decimal_places=2, help_text='Enter a duration in hours (e.g. 1.50)', max_digits=3, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))]),
        ),
    ]