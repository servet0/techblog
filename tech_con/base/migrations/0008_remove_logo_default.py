# Generated by Django 4.2.5 on 2023-09-13 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_logo_default'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logo',
            name='default',
        ),
    ]
