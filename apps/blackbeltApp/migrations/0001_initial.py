# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 17:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginRegister', '0002_auto_20160727_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='loginRegister.User')),
                ('userswant', models.ManyToManyField(related_name='userswant', to='loginRegister.User')),
            ],
            managers=[
                ('itemManager', django.db.models.manager.Manager()),
            ],
        ),
    ]
