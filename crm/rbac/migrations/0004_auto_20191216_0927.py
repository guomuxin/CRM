# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-12-16 01:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0003_permission_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('icon', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='permission',
            name='is_menu',
        ),
        migrations.AddField(
            model_name='permission',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rbac.Menu'),
        ),
    ]
