# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-27 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0015_auto_20170727_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='q_count',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='test',
            name='timetest',
            field=models.PositiveIntegerField(default=2),
        ),
    ]
