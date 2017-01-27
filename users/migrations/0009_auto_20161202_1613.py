# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20161202_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bank_guarantee_certificate',
            field=models.ImageField(null=True, upload_to=b'bank_guarantees/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='user',
            name='business_certificate',
            field=models.ImageField(null=True, upload_to=b'business_certificates/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='user',
            name='kra_pin_certificate',
            field=models.ImageField(null=True, upload_to=b'kra_pins/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='user',
            name='national_id_photo',
            field=models.ImageField(null=True, upload_to=b'national_id_photos/%Y/%m/%d/'),
        ),
    ]