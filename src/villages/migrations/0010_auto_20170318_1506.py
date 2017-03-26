# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-18 14:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camps', '0020_camp_read_only'),
        ('villages', '0009_auto_20161229_2143'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='village',
            unique_together=set([('slug', 'camp')]),
        ),
    ]