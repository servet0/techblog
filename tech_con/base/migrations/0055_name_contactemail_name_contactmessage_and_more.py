# Generated by Django 4.2.5 on 2023-09-21 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0054_remove_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='name',
            name='contactemail',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='name',
            name='contactmessage',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='name',
            name='contactname',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='name',
            name='contactphone',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='name',
            name='contactsend',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='name',
            name='contactsubject',
            field=models.TextField(blank=True, null=True),
        ),
    ]
