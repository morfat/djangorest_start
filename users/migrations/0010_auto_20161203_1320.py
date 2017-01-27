# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-03 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20161202_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='bank_guarantee_certificate',
            field=models.ImageField(null=True, upload_to='bank_guarantees/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='business_certificate',
            field=models.ImageField(null=True, upload_to='business_certificates/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='kra_pin_certificate',
            field=models.ImageField(null=True, upload_to='kra_pins/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='national_id_photo',
            field=models.ImageField(null=True, upload_to='national_id_photos/%Y/%m/%d/'),
        ),
    ]
