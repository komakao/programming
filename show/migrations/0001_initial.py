# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-28 04:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import show.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShowGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('classroom_id', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=250)),
                ('number', models.CharField(max_length=30)),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('picture', models.ImageField(default=b'/static/show/null.jpg', upload_to=show.models.upload_path_handler)),
                ('done', models.BooleanField(default=False)),
                ('open', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ShowReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_id', models.IntegerField(default=0)),
                ('student_id', models.IntegerField(default=0)),
                ('score1', models.IntegerField(default=0)),
                ('score2', models.IntegerField(default=0)),
                ('score3', models.IntegerField(default=0)),
                ('comment', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]