# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-19 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0006_auto_20170619_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='qquery',
            field=models.TextField(default=''),
        ),
    ]
