# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-12 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0019_auto_20170727_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='activatecode',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]