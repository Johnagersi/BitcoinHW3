# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-05 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='total_buy_sell_deposit_withdraw',
            field=models.IntegerField(),
        ),
    ]
