# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-02 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_auto_20170102_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_by',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
