# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_repository'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='technology',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]