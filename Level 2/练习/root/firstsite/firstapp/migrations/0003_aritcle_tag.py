# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 01:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_aritcle'),
    ]

    operations = [
        migrations.AddField(
            model_name='aritcle',
            name='tag',
            field=models.CharField(blank=True, choices=[('tech', 'Tech'), ('life', 'Life')], max_length=5, null=True),
        ),
    ]
