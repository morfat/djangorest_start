# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 23:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_certificate'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='national_id_photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]