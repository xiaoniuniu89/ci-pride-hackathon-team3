# Generated by Django 3.2 on 2022-06-19 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0009_auto_20220619_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donations',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
