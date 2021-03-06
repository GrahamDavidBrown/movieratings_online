# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 00:25
from __future__ import unicode_literals

from django.db import migrations, models
import csv


def load_raters(apps, schema_editor):
    Rater = apps.get_model("movieratings_app", "Rater")
    datafile_PATH = 'u.user'

    with open(datafile_PATH, 'r', encoding="latin-1") as f:
        cats = {'fieldnames': ('rater_id', 'age', 'gender', 'occupation', 'zip_code'), 'delimiter': ('|')}
        reader = csv.DictReader(f, **cats)
        for row in reader:
            r = Rater(id=row['rater_id'], age=row['age'], gender=row['gender'], occupation=row['occupation'], zip_code=row['zip_code'])
            r.save()

class Migration(migrations.Migration):

    dependencies = [
        ('movieratings_app', '0003_auto_20170316_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rater',
            name='zip_code',
            field=models.CharField(max_length=10)),

        migrations.RunPython(load_raters)
    ]
