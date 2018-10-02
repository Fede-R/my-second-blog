# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_enfermedadmara'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviewmaes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enfermedadName', models.CharField(max_length=50)),
                ('enfermedadId', models.IntegerField()),
                ('comment', models.TextField()),
                ('reviewer', models.CharField(max_length=50)),
                ('stars', models.IntegerField()),
                ('createdTime', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reviewmara',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enfermedadName', models.CharField(max_length=50)),
                ('enfermedadId', models.IntegerField()),
                ('comment', models.TextField()),
                ('reviewer', models.CharField(max_length=50)),
                ('stars', models.IntegerField()),
                ('createdTime', models.DateField(auto_now=True)),
            ],
        ),
    ]
