# Generated by Django 4.2.5 on 2023-09-14 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_header_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='view',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
