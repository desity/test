# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-13 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tquestion',
            old_name='choicer',
            new_name='choice5',
        ),
        migrations.AddField(
            model_name='applicant',
            name='test_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tquestion',
            name='choicer1',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='tquestion',
            name='choicer2',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='tquestion',
            name='choicer3',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='tquestion',
            name='choicer4',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='tquestion',
            name='choicer5',
            field=models.BooleanField(default='False'),
        ),
    ]
