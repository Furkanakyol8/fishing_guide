# Generated by Django 4.2.1 on 2023-05-16 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishes', '0003_fishes_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fishes',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]