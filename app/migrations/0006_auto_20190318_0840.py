# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-03-18 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190318_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_image',
            field=models.ImageField(blank=True, upload_to='employees/'),
        ),
    ]