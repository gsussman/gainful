# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 19:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20160809_1347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='message',
            new_name='custom_message',
        ),
    ]