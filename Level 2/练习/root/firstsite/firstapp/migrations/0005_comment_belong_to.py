# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 15:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_auto_20161115_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='belong_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='under_comments', to='firstapp.Aritcle'),
        ),
    ]
