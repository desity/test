# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-21 13:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0008_auto_20170621_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='passing_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 21, 16, 24, 17, 946746)),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='startpassing_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 21, 16, 24, 17, 946746)),
        ),
    ]
