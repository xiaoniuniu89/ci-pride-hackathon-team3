# Generated by Django 3.2 on 2022-06-18 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_event_slug_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='featured_image',
            field=models.ImageField(default='default.jpg', upload_to='media'),
        ),
    ]