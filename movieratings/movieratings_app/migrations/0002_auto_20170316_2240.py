# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-16 22:40
from __future__ import unicode_literals

from django.db import migrations
import csv

def load_movies(apps, schema_editor):
    Movie = apps.get_model("movieratings_app", "Movie")
    datafile_PATH = 'u.item'

    with open(datafile_PATH, 'r', encoding="latin-1") as f:
        cats = {'fieldnames': ('movie_id', 'title', 'release_date', 'imdb_link')}
        reader = csv.DictReader(f, **cats, delimiter = '|')
        for row in reader:
            m = Movie(id=row['movie_id'], title=row['title'], release_date=row['release_date'], imdb_link=row['imdb_link'])
            m.save()


# do the same for raters and ratings
# call movie, rater and rating objects in load_ratings()
# be sure to fill in user id from rater and movie if from movie for load_ratings()

class Migration(migrations.Migration):

    dependencies = [
        ('movieratings_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_movies)
    ]
