# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-08 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=100)),
                ('img2', models.CharField(max_length=100)),
            ],
        ),
    ]
