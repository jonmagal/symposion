# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-17 18:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_schedule', '0002_slot_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='title',
            field=models.TextField(verbose_name='Title'),
        ),
    ]