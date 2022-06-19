# Generated by Django 3.2 on 2022-06-19 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0015_auto_20220618_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='charities',
            field=models.CharField(choices=[('Consent Workshop', 'Consent Workshop'), ('Outright International', 'Outright International'), ('GlobalGiving', 'Global Giving'), ('MicroRainbow', 'Micro Rainbow')], default='ConsentWorkshop', max_length=22),
            preserve_default=False,
        ),
    ]