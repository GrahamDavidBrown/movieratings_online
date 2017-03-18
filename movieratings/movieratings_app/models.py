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
        avg_rating_list = sorted(avg_rating_list, key=lambda x: x[1])
        return avg_rating_list[:n]

    def __repr__(self):
        return "{} {}".format(self.title, self.imdb_link)


class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=10)

    def get_top_5_unseen_movies(Rater):
        '''if a rater rated the movies, they have seen them.'''
        '''so a rater in the ratings table has the seen the movie'''
        sort_ratings_by_rater = Rating.objects.filter(Rater)
        seen_movie_set = [set(movie, movie.id) for rating in sort_ratings_by_rater]
        seen_movies = Movies.objects.filter(movie)
        all_movies_set = set(Movies.objects.all())
        unseen_movies_Set = all_movies_set - seen_movie_top
        return unseen_moives[:5]

    def get_total_avg_ratings(Rater):
        '''averages all ratings'''
        all_ratings_by_rater = Rating.objects.filter(Rater)
        all_ratings = [rating for rating in all_ratings_by_rater.rating]
        total = 0
        for rate in all_ratings:
            total += rate
        return total / len(all_ratings)

    def get_eucl_distance(rater1, raster2):
        """gets eucl distance, 1 is perfect match, measures user compatibility"""
        user1list = Rating.objects.filter(rater1)
        user2list = Rating.objects.filter(rater2)
        intersection_of_lists = [val for val in user1list if val in user2list]
        weighted = len(intersection_of_lists)
        if len(user1list) is 0:
            return 0
        differences = [user1list[idx] - user2list[idx] for idx in range(len(user1list))]
        squares = [diff ** 2 for diff in differences]
        sum_of_squares = sum(squares)
        return (1 / (1 + (sum_of_squares**(0.5)))) * weighted

    def recommend_movie(Rater, n):
        """movie recommendation algorithm"""
        all_raters = Rating.objects.all()
        sim_rater_list = [((Rater.get_eucl_distance((all_raters.pop()) for rater in all_raters)))]
        most_sim_rater_list = sorted(sim_rater_list)[:10]
        return most_sim_rater_list


class Rating(models.Model):
    rater = models.ForeignKey(Rater, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
    timestamp = models.IntegerField()
