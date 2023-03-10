# Generated by Django 3.2.17 on 2023-02-14 05:33

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10, unique=True)),
                ('details', models.CharField(max_length=50)),
                ('rate', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('total_target', models.IntegerField()),
                ('current_donation', models.IntegerField(default=0)),
                ('start_campaign', models.DateField(blank=True, default=datetime.datetime.now)),
                ('end_campaign', models.DateField()),
                ('created_at', models.DateField(blank=True, default=datetime.datetime.now)),
                ('selected_at_by_admin', models.BooleanField(default=False)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectsapp.category')),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Projects_pictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/Projects/%y/%m/%d')),
                ('ProjectId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projectsapp.project')),
            ],
        ),
    ]
