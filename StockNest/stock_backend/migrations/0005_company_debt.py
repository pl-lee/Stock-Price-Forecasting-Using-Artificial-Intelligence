# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-29 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_backend', '0004_company_maxval'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='debt',
            field=models.FloatField(default=0),
        ),
    ]