# Generated by Django 3.2 on 2022-06-19 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0017_alter_donation_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='charities',
            new_name='charity',
        ),
    ]
