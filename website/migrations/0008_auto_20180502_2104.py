# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-02 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20180502_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(default='<Noname>', max_length=255),
        ),
    ]
