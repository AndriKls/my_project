# Generated by Django 5.1.1 on 2024-11-24 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_movies_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movies',
            options={'verbose_name': 'Movie', 'verbose_name_plural': 'Movies'},
        ),
    ]
