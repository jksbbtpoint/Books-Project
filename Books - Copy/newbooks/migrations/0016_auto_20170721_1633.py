# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-21 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newbooks', '0015_auto_20170721_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oldorderadd',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
