# Generated by Django 3.1.7 on 2021-06-03 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20210603_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_poster',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='event',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]