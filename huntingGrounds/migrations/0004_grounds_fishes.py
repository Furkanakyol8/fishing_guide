# Generated by Django 4.2.1 on 2023-05-25 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishes', '0009_fishes_category'),
        ('huntingGrounds', '0003_alter_grounds_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='grounds',
            name='fishes',
            field=models.ManyToManyField(to='fishes.fishes'),
        ),
    ]
