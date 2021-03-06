# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 12:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0006_host_num_cpus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u54c1\u724c\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u8bbe\u5907\u54c1\u724c',
                'verbose_name_plural': '\u8bbe\u5907\u54c1\u724c',
            },
        ),
        migrations.AddField(
            model_name='host',
            name='brand',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.Device', verbose_name='\u8bbe\u5907\u54c1\u724c'),
        ),
    ]
