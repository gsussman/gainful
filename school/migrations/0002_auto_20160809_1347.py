# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-09 13:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='audience_grp',
            new_name='audience_Groups',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='audience_ind',
            new_name='audience_Individuals',
        ),
    ]
