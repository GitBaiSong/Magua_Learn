# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 03:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_aritcle_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='people',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
