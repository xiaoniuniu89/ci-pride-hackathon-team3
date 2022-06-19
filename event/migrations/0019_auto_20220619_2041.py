# Generated by Django 3.2 on 2022-06-19 20:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0018_rename_charities_event_charity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='volunteer_list',
        ),
        migrations.AlterField(
            model_name='event',
            name='charity',
            field=models.CharField(choices=[('Consent Workshop', 'Consent Workshop'), ('Outright International', 'Outright International'), ('Global Giving', 'Global Giving'), ('Micro Rainbow', 'Micro Rainbow')], max_length=22),
        ),
        migrations.CreateModel(
            name='VolunteerList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volunteers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]