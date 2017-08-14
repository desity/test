# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-29 16:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0012_auto_20170622_1052'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('regdate', models.DateTimeField(default=django.utils.timezone.now)),
                ('veryfied', models.BooleanField(default='False')),
                ('active', models.BooleanField(default='False')),
                ('comment', models.CharField(max_length=50)),
            ],
        ),
    ]