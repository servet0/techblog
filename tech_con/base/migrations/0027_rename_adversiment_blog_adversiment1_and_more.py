# Generated by Django 4.2.5 on 2023-09-15 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='adversiment',
            new_name='adversiment1',
        ),
        migrations.AddField(
            model_name='blog',
            name='adversiment2',
            field=models.ImageField(blank=True, null=True, upload_to='ads'),
        ),
        migrations.AddField(
            model_name='blog',
            name='adversiment3',
            field=models.ImageField(blank=True, null=True, upload_to='ads'),
        ),
    ]
