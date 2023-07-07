# Generated by Django 4.2.3 on 2023-07-05 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='myapp/images/carousel')),
                ('label', models.CharField(max_length=25)),
                ('content', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=75)),
                ('desc', models.CharField(default='', max_length=500)),
                ('price', models.CharField(default=0, max_length=50)),
                ('image', models.ImageField(default='', upload_to='myapp/images')),
                ('like_count', models.PositiveIntegerField(default=0)),
                ('comment_count', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
