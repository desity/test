# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-22 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0010_auto_20170621_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='status_description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
