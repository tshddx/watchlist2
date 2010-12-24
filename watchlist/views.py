from watchlist2.watchlist.models import *
from annoying.decorators import render_to
from operator import itemgetter
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Count, Q
from django import forms
# from tmdb_search import tmdb_search
from themoviedb import tmdb
import csv
from itertools import islice

@render_to('index.html')
def index(request):
    recent_viewings = Viewing.objects.order_by('-date')[:10]
    directors = sorted([(x, x.movie_set.count()) for x in Person.objects.all()], key=itemgetter(1), reverse=True)
    favorite_directors = directors[:10]
    wish_list = Movie.objects.annotate(num_viewings=Count('viewing')).filter(num_viewings__exact=0)
    return {'recent_viewings': recent_viewings, 'favorite_directors': favorite_directors, 'wish_list': wish_list}
    
@render_to('movie_detail.html')
def movie_detail(request, title=None, tmdb_id=None):
    # If POST, potentially creates a new Movie object:
    if request.method == 'POST' and tmdb_id:
        if 'just-watched' in request.POST:
            movie = Movie.movie_from_tmdb_id(request.POST['tmdb_id'])
            movie.add_viewing()
        elif 'add-to-wish-list' in request.POST:
            movie = Movie.movie_from_tmdb_id(request.POST['tmdb_id'])
        else:
            raise Exception("If posting to movie_detail, must send either 'just-watched' or 'add-to-wish-list'.")
        movie.save()
        return HttpResponseRedirect(movie.get_absolute_url())
    if title:
        movie = get_object_or_404(Movie, title=title)
    elif tmdb_id:
        movie = get_object_or_404(Movie, tmdb_id=tmdb_id)
    viewings = movie.viewing_set.order_by('-date')
    return {'movie': movie, 'viewings': viewings}
    
@render_to('person_detail.html')
def person_detail(request, name):
    person = get_object_or_404(Person, name=name)
    movies = person.movie_set.all()
    return {'person': person, 'movies': movies}
    
@render_to('movie_list.html')
def movie_list(request):
    viewings = Viewing.objects.order_by('-date')
    return {'viewings': viewings}
    
@render_to('wish_list.html')
def wish_list(request):
    wish_list = Movie.objects.annotate(num_viewings=Count('viewing')).filter(num_viewings__exact=0)
    return {'wish_list': wish_list}
    
@render_to('person_list.html')
def person_list(request):
    people = Person.objects.all()
    return {'people': people}
   
@render_to()
def movie_search(request):
    
    def get_thumbnail(movie_result):
        for image in movie_result['images']:
            if image['type'] == 'poster':
                return image['thumb']
        return None

    if request.method == 'POST':
        titles = []
        movies = []
        if 'single-movie-search' in request.POST:
            titles = [request.POST['query']]
        else:
            titles = [line for line in request.POST['movies_list'].splitlines() if line]
        for movie_title in titles:
            results = tmdb.search(movie_title)[:3]
            for result in results:
                result['thumb'] = get_thumbnail(result)
                result['in_watchlist'] = Movie.objects.filter(tmdb_id=result['id']).count() != 0
            movies.append((movie_title, results))
        return {'movies': movies, 'TEMPLATE': 'movie_search_results.html'}
    return {'fun': 'fun', 'TEMPLATE': 'movie_search.html'}

@render_to('person_search_results.html')
def person_search(request):
    if request.method == 'POST' and 'person-search' in request.POST:
        terms = request.POST['query'].split()
        queries = []
        for term in terms:
            queries.append(Q(name__icontains=term))
        if queries:
            people = Person.objects.filter(reduce(lambda x, y: x & y, queries))
        else:
            people = None
    return {'people': people, 'query': request.POST['query']}

# @render_to()
# def movie_import(request):
#     if request.method == 'POST':
#         form = UploadCsvForm(request.POST, request.FILES)
#         if form.is_valid():
#             file = request.FILES['file']
#             if file.size > 50000:
#                 return HttpResponse("This file should only be a few dozen kilobytes.")
#             reader = csv.reader(file)
#             movies = []
#             for line in islice(reader, 30, 33):
#                 if ((line[0] != "Title") and line[2] and line[3] and line[4] and line[5]):
#                     title = line[0]
#                     release_date = date(int(line[2]), 1, 1)
#                     year = int(line[2])
#                     runtime = line[4]
#                     nationality = line[3]
#                     view_date = line[5]
#                     comments = line[7] if len(line) == 8 else ""
#                     results = tmdb_search(title, num_results=3)
#                     movies.append((title, year, view_date, results))
#             return {'movies': movies, 'TEMPLATE': 'movie_import_results.html'}
#     else:
#         form = UploadCsvForm()
#     return {'form': form, 'TEMPLATE': 'movie_import.html'}
