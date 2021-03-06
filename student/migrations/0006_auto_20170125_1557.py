# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-25 07:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20170125_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_id', models.IntegerField(default=0)),
                ('filename', models.TextField()),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='work',
            name='uuid',
        ),
    ]
