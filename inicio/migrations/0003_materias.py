# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-04 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_auto_20210227_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_materia', models.IntegerField()),
                ('nombre', models.CharField(max_length=20, verbose_name='nombre')),
            ],
        ),
    ]
