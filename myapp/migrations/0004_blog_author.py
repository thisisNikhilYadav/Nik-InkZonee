# Generated by Django 4.2.3 on 2023-07-05 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_blog_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(default='', max_length=75),
        ),
    ]
