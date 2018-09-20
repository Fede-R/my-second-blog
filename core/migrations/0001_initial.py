# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enfermedad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('images', models.IntegerField()),
                ('planta', models.CharField(max_length=50)),
                ('sintomaAA', models.CharField(max_length=50)),
                ('sintomaBB', models.CharField(max_length=50)),
                ('sintomaCC', models.CharField(max_length=50)),
                ('sintomaDD', models.CharField(max_length=50)),
                ('sintomaEE', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
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
            name='Suggestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enfermedadName', models.CharField(max_length=50)),
                ('enfermedadId', models.IntegerField()),
                ('attribute', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
