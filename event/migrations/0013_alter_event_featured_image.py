# Generated by Django 3.2 on 2022-06-18 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0012_alter_event_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='featured_image',
            field=models.ImageField(default='default.jpg', upload_to='media'),
        ),
    ]
