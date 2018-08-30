# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-07 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_backend', '0006_auto_20170829_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='assetTurnover',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='company',
            name='currentRatio',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='company',
            name='marketCap',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='company',
            name='marketSentiments',
            field=models.FloatField(default=-1),
        ),
        migrations.AddField(
            model_name='company',
            name='marketSentimentsInfo',
            field=models.CharField(default='0', max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='marketSubjectivity',
            field=models.FloatField(default=-1),
        ),
        migrations.AddField(
            model_name='company',
            name='profitMargin',
            field=models.FloatField(default=0),
        ),
    ]
