# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_conference', '0002_auto_20170711_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='abbrv',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
