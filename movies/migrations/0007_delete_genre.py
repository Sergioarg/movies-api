# Generated by Django 5.0.6 on 2024-06-02 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_remove_movie_adult'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Genre',
        ),
    ]
