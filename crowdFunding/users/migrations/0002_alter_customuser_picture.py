# Generated by Django 4.1.6 on 2023-02-28 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='picture',
            field=models.ImageField(default=1, upload_to='media/'),
            preserve_default=False,
        ),
    ]
