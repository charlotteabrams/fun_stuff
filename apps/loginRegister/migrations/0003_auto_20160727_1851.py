# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 18:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginRegister', '0002_auto_20160727_1631'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]
