# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-03-19 19:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20190318_1106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='employee_image',
        ),
    ]
