# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-12-05 07:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='telephone',
            new_name='phone_number',
        ),
    ]
