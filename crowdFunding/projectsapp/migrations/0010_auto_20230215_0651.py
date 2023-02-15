# Generated by Django 3.2.18 on 2023-02-15 06:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectsapp', '0009_alter_projectrating_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='commentreport',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='projectreport',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='replay',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='replayreport',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]