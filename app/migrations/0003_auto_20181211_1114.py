# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-11 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]