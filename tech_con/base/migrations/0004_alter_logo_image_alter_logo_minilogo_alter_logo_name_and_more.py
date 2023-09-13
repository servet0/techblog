# Generated by Django 4.2.5 on 2023-09-13 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_logo_minilogo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='logo'),
        ),
        migrations.AlterField(
            model_name='logo',
            name='minilogo',
            field=models.ImageField(blank=True, null=True, upload_to='minilogo'),
        ),
        migrations.AlterField(
            model_name='logo',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='logo',
            name='tittle',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
