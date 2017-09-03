# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('repo_count', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]