# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-25 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='number',
        ),
        migrations.AddField(
            model_name='work',
            name='file',
            field=models.FileField(default=b'/static/certificate/null.jpg', upload_to=b'static/work'),
        ),
    ]