# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-25 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20170125_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='file_uuid',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='work',
            name='file',
            field=models.FileField(upload_to=b''),
        ),
    ]