from django.test import TestCase
from movieratings_app import models


class ModelsTestCase(TestCase):
    def setUp(self):
        models.Rating.objects.create(rater_id = 12, movie_id = 1, rating = 3, timestamp = 123456789)
        models.Rating.objects.create(rater_id = 34, movie_id = 1, rating = 5, timestamp = 187654321)

    def test_get_avg_rating(self):
        r1 = models.Rating.objects.get(rater_id=12)
        r2 = models.Rating.objects.get(rater_id=34)
        assert models.Movie.get_avg_rating(r1.movie_id) == 4

if __name__ == "__main__":
    unittest.main()
