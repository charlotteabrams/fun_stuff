# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blackbeltApp', '0003_auto_20160727_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]