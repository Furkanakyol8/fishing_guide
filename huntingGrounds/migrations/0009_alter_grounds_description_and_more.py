# Generated by Django 4.2.1 on 2023-05-26 11:47

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('huntingGrounds', '0008_alter_grounds_summarizeddescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grounds',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='grounds',
            name='summarizedDescription',
            field=models.CharField(blank=True, max_length=99999, null=True),
        ),
    ]