# Generated by Django 4.2.5 on 2023-09-14 19:45

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_remove_header_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='header2',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='header2',
            name='view',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
