# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 10:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170809_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vertifyregister',
            name='vertifytime',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 9, 10, 26, 23, 25226)),
        ),
    ]