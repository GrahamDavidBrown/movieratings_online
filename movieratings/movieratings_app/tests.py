from django.conf import settings
settings.configure()
from django.test import TestCase
from .models import Movie


def test_get_avg_rating():
    assert Movie.get_avg_rating(1) > 3 and Movie.get_avg_rating(1) < 5
