# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-26 21:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_message_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagefile',
            name='before_name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
