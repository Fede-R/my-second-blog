# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_enfermedadmaes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enfermedadmara',
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
    ]
