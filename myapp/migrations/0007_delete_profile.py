# Generated by Django 4.2.3 on 2023-07-06 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_user_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]