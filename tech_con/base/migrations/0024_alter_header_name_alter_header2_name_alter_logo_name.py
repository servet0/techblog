# Generated by Django 4.2.5 on 2023-09-15 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0023_mainadversiment_name_alter_header_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='header2',
            name='name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='logo',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
