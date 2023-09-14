# Generated by Django 4.2.5 on 2023-09-14 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_remove_header_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Header2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]