# Generated by Django 3.2.17 on 2023-02-14 10:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projectsapp', '0006_auto_20230214_0953'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Test',
            new_name='Test2',
        ),
        migrations.AlterField(
            model_name='project',
            name='details',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
