# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-12 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newbooks', '0076_selectadd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selectadd',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='selectadd',
            name='select',
            field=models.IntegerField(null=True),
        ),
    ]