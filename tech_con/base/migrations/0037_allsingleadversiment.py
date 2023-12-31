# Generated by Django 4.2.5 on 2023-09-16 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0036_blog_urladver1_blog_urladver2_blog_urladver3_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllSingleAdversiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('ads1', models.ImageField(blank=True, null=True, upload_to='ads')),
                ('urlads1', models.URLField(blank=True, null=True)),
                ('ads2', models.ImageField(blank=True, null=True, upload_to='ads')),
                ('urlads2', models.URLField(blank=True, null=True)),
                ('ads3', models.ImageField(blank=True, null=True, upload_to='ads')),
                ('urlads3', models.URLField(blank=True, null=True)),
                ('ads4', models.ImageField(blank=True, null=True, upload_to='ads')),
                ('urlads4', models.URLField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
