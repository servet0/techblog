# Generated by Django 4.2.5 on 2023-09-16 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0033_mainadversiment_urlnavbar'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainadversiment',
            name='urlads',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mainadversiment',
            name='urlads2',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mainadversiment',
            name='urlads3',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mainadversiment',
            name='urlads4',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mainadversiment',
            name='urlheaderurl',
            field=models.URLField(blank=True, null=True),
        ),
    ]
