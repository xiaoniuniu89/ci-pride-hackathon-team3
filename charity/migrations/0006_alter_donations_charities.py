# Generated by Django 3.2 on 2022-06-18 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0005_donations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donations',
            name='charities',
            field=models.CharField(choices=[(1, 'Consent Workshop'), (2, 'Outright International'), (3, 'Global Giving'), (4, 'Micro Rianbow')], max_length=2),
        ),
    ]
