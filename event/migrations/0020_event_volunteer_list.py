# Generated by Django 3.2 on 2022-06-19 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0019_auto_20220619_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='volunteer_list',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='event.volunteerlist'),
        ),
    ]
