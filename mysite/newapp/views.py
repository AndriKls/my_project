from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator
# Create your views here.


def movie_list(request):
    movies = Movies.objects.all()

    movie_title = request.GET.get('movie_title')

    if movie_title != '' and movie_title is not None:
        movies = movies.filter(title__icontains=movie_title)

    paginator = Paginator(movies, 5)
    page = request.GET.get('page')
    movies = paginator.get_page(page)
    context = {
        'movies': movies,
    }
    return render(request, 'newapp/movie_list.html', context)