# Generated by Django 4.2.5 on 2023-09-15 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_blog_adversiment4'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='adversimenthome',
            field=models.ImageField(blank=True, null=True, upload_to='ads'),
        ),
    ]
