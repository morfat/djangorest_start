# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-10 23:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_auto_20170104_0232'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(null=True, upload_to='profile_photos/%Y/%m/%d/'),
        ),
    ]