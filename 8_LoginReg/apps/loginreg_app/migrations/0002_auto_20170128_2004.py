# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 20:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginreg_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='brithday',
            new_name='birthday',
        ),
    ]
