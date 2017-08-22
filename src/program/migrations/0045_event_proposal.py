# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-22 08:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0044_auto_20170801_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='proposal',
            field=models.OneToOneField(blank=True, help_text='The event proposal object this event was created from', null=True, on_delete=django.db.models.deletion.CASCADE, to='program.EventProposal'),
        ),
    ]
