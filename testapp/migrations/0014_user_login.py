# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-29 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0013_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
