# Generated by Django 4.2.5 on 2023-09-15 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0029_blog_adversimenthome'),
    ]

    operations = [
        migrations.RenameField(
            model_name='header',
            old_name='adversiment',
            new_name='adversiment1',
        ),
        migrations.RenameField(
            model_name='header2',
            old_name='adversiment',
            new_name='adversiment1',
        ),
        migrations.AddField(
            model_name='header',
            name='adversiment3',
            field=models.ImageField(blank=True, null=True, upload_to='ads'),
        ),
        migrations.AddField(
            model_name='header',
            name='adversiment4',
            field=models.ImageField(blank=True, null=True, upload_to='ads'),
        ),
        migrations.AddField(
            model_name='header2',
            name='adversiment3',
            field=models.ImageField(blank=True, null=True, upload_to='ads'),
        ),
        migrations.AddField(
            model_name='header2',
            name='adversiment4',
            field=models.ImageField(blank=True, null=True, upload_to='ads'),
        ),
    ]
