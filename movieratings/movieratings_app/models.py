from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.CharField(max_length=15)
    imdb_link = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)

    def get_avg_rating(movie_id):
        all_ratings = Rating.objects.filter(movie_id=movie_id)
        sum_of_ratings = 0
        len_of_ratings = len(all_ratings)
        for item in all_ratings:
            sum_of_ratings += item.rating
        return (sum_of_ratings/len_of_ratings)

        # figure out correct iterable for get_avg_ratings
    def get_top_n_movies_by_rating(n):
        all_ratings = Rating.objects.all()
        avg_rating_list = [(m_rate.movie.id, Movie.get_avg_rating(m_rate.movie.id)) for m_rate in all_ratings]
        return avg_rating_list[:n]

class Rater(models.Model):
    age = models.IntegerField() # invalid literal
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=10)

    def get_top_n_unseen_movies():
        pass

    def get_total_avg_ratings():
        pass


class Rating(models.Model):
    rater = models.ForeignKey(Rater, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
    timestamp = models.IntegerField()
