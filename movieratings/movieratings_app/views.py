from django.shortcuts import render
from .models import Movie, Rating


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
