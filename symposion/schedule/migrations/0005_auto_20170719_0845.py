# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-19 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_schedule', '0004_auto_20170719_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='name',
            field=models.CharField(editable=False, max_length=255),
        ),
    ]
