# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-22 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0011_applicant_status_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='status_description',
            field=models.CharField(max_length=50),
        ),
    ]