# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-09 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newbooks', '0033_auto_20170809_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pic',
            field=models.FileField(default='/static/na.jpg', upload_to='pic'),
        ),
    ]