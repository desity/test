# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 07:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('passing_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('mark_pass', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=50)),
                ('q_count', models.IntegerField(default=1)),
                ('test_descr', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tquestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, null=True)),
                ('choice1', models.CharField(max_length=200)),
                ('choice2', models.CharField(max_length=200)),
                ('choice3', models.CharField(max_length=200)),
                ('choice4', models.CharField(max_length=200)),
                ('choicer', models.CharField(max_length=200)),
                ('test_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Test')),
            ],
        ),
    ]