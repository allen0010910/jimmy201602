# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 09:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webterminal', '0006_auto_20171126_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='sshlog',
            name='height',
            field=models.PositiveIntegerField(default=40),
        ),
        migrations.AddField(
            model_name='sshlog',
            name='width',
            field=models.PositiveIntegerField(default=90),
        ),
    ]