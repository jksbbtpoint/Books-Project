# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-07 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newbooks', '0069_auto_20171206_2013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resetpass',
            old_name='purchase_date',
            new_name='create_date',
        ),
        migrations.AlterField(
            model_name='resetpass',
            name='serialid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]