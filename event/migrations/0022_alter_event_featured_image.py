# Generated by Django 3.2 on 2022-06-19 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0021_auto_20220619_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='featured_image',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]
