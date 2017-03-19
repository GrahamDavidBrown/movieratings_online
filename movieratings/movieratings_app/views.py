from django.shortcuts import render
from .models import Movie, Rating
from django.contrib.auth.models import User



# Create your views here.
def top_20_movies(request):
    context = {}
    top_20 = Movie.get_top_n_movies_by_rating(20)
    context['top_20'] = top_20
    return render(request, 'movieratings_app/top_20_movies.html', context)


def movie_detail(request, movie_id=1):  # needs to work with all movie_ids
    m = Movie.objects.get(id=movie_id)
    r = Rating.objects.filter(movie_id=movie_id)
    rater_list = []
    for item in r:
        rater_list.append(item.rater+'\n')
    context = {'movie_title': m.title, 'avg_rating': m.get_avg_rating(),
    'rater_list': rater_list}

    return render(request, 'movieratings_app/movie_detail.html', context)


def top_5_unseen(request):
    top_5_unseen = get_top_5_unseen_movies()
    context = {'top_5_unseen': top_5_unseen}
    return render(request, 'movieratings_app/top_5_unseen', context)


def dashboard(request):
    username = request.user
    user_info = User.objects.get(username=username)
    username = user_info.username
    password = user_info.password
    first_name = user_info.first_name
    last_name = user_info.last_name
    user_ratings = Rating.objects.filter(id=user_info.id)
    movie_rating_list = [(rating.movie, rating.rating) for rating in user_ratings]
    context = {'username': username, 'password': password, 'first_name': first_name,
    "last_name": last_name, 'user_ratings': movie_rating_list}
    return render(request, "movieratings_app/pub_profile.html", context)


def profile(request):
    username = request.user
    user_info = User.objects.get(username=username)
    username = user_info.username
    password = user_info.password
    first_name = user_info.first_name
    last_name = user_info.last_name
    user_ratings = Rating.objects.filter(rater=user_info.id)
    movie_rating_list = [(rating.movie, rating.rating) for rating in user_ratings]
    context = {'username': username, 'password': password, 'first_name': first_name,
    "last_name": last_name, 'user_ratings': movie_rating_list, "sep": '    '}
    return render(request, "movieratings_app/profile.html", context)


def delete_entry(request):
    Rating.objects.get(pk=name).delete()
    return render(request, "movierating_app/profile.html", context)
