# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 13:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_comments_comments_from'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comments_from',
        ),
    ]
