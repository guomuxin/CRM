# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-12-06 10:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20191206_1817'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='telephone',
            new_name='phone_number',
        ),
    ]
