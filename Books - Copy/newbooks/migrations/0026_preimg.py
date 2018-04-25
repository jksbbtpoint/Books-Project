# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-26 06:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newbooks', '0025_auto_20170725_2215'),
    ]

    operations = [
        migrations.CreateModel(
            name='preimg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic1', models.FileField(blank=True, null=True, upload_to='pic')),
                ('pic2', models.FileField(blank=True, null=True, upload_to='pic')),
                ('fkbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newbooks.book')),
            ],
        ),
    ]
