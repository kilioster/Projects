# Generated by Django 5.0.4 on 2024-05-09 00:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=13)),
                ('description', models.TextField()),
                ('company', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
