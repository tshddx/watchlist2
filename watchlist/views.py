from watchlist.models import *
from annoying.decorators import render_to
from operator import itemgetter
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Count, Q, Max
from django import forms
# from tmdb_search import tmdb_search
from themoviedb import tmdb
import tmdb_person
import csv
from itertools import islice

def get_movie_thumbnail(movie_result):
    for image in movie_result['images']:
        if image['type'] == 'poster':
            return image['thumb']
    return None

def get_movie_imdb_id(tmdb_id):
    return tmdb.getMovieInfo(tmdb_id)['imdb_id']

def get_person_thumbnail(tmdb_id):
    person = tmdb_person.getPersonInfo(tmdb_id)
    if 'thumbnail' in person:
        return person['thumbnail']

@render_to('index.html')
def index(request):
    recent_viewings = Viewing.objects.select_related('movie__director').annotate(num_viewings=Count('movie__viewing')).order_by('-date')[:10]
    favorite_directors = Person.objects.annotate(num_movies=Count('movie')).order_by('-num_movies')[:5]
    wish_list = Movie.objects.select_related('director').annotate(num_viewings=Count('viewing')).filter(num_viewings__exact=0).filter(recommended_by__isnull=True).order_by("-id")[:10]
    recommended_movies = Movie.objects.select_related('director').annotate(num_viewings=Count('viewing')).filter(num_viewings__exact=0).filter(recommended_by__isnull=False).order_by("-id")[:9]
    return {'recent_viewings': recent_viewings, 'favorite_directors': favorite_directors, 'wish_list': wish_list, 'recommended_movies': recommended_movies}
    
@render_to('movie_detail.html')
def movie_detail(request, title):

    class MovieCommentsForm(forms.ModelForm):
        class Meta:
            model = Movie
            fields = ('comments',)
            
    movie = get_object_or_404(Movie.objects.select_related('director'), title=title)
    comments_form = MovieCommentsForm()
    if request.method == 'POST':
        if not request.user.is_authenticated():
            return HttpResponse("You must be authenticated to do this.")
        if 'save-comments' in request.POST:
            comments_form = MovieCommentsForm(data=request.POST, instance=movie)
            if comments_form.is_valid():
                comments_form.save()
    else:
        comments_form = MovieCommentsForm(instance=movie)
    viewings = movie.viewing_set.order_by('-date')
    if movie.tmdb_id:
        image_url = get_movie_thumbnail(tmdb.getMovieInfo(movie.tmdb_id))
        imdb_id = get_movie_imdb_id(movie.tmdb_id)
    return {'movie': movie, 'viewings': viewings, 'comments_form': comments_form, 'image_url': image_url, 'imdb_id': imdb_id}

def movie_detail_by_id(request, tmdb_id):
    # If posting to this view, it's coming from one of the movie_buttons. This potentially creates a new Movie instance.
    if request.method == 'POST':
        movie = Movie.movie_from_tmdb_id(request.POST['tmdb_id'])
        if 'add-to-wish-list' in request.POST:
            if not request.user.is_authenticated():
                return HttpResponse("You must be authenticated to do this.")
            c = request.POST['comments']
            if c:
                movie.comments = c
        if 'just-watched' in request.POST:
            if not request.user.is_authenticated():
                return HttpResponse("You must be authenticated to do this.")
            d = request.POST['date']
            d = datetime.date(*map(int, d.split('-')))
            n = request.POST['notes']
            if n:
                movie.add_viewing(d, notes=n)
            else:
                movie.add_viewing(d)
        if 'recommend' in request.POST:
            movie.recommended_by = request.POST['recommended_by']
            if request.POST['recommend_comments']:
                movie.recommend_comments = request.POST['recommend_comments']
        movie.save()
    # If not posting to this view, redirect to the normal movie url.
    else:
        movie = get_object_or_404(Movie, tmdb_id=tmdb_id)
    return HttpResponseRedirect(movie.get_absolute_url())
    
@render_to('person_detail.html')
def person_detail(request, name):
    person = get_object_or_404(Person, name=name)
    movies = person.movie_set.all().annotate(num_viewings=Count('viewing'))
    if person.tmdb_id:
        image_url = get_person_thumbnail(person.tmdb_id)
    return {'person': person, 'movies': movies, 'image_url': image_url}
    
@render_to('movie_list.html')
def movie_list(request):
    movies = Movie.objects.annotate(num_viewings=Count('viewing'), most_recent_viewing=Max('viewing__date')).select_related('director').order_by("-id")
    movies = movies.exclude(num_viewings=0)
    return {'movies': movies}
    
@render_to('wish_list.html')
def wish_list(request):
    recommended_movies = Movie.objects.select_related('director').annotate(num_viewings=Count('viewing')).filter(num_viewings__exact=0).filter(recommended_by__isnull=False).order_by("-id")[:10]
    wish_list = Movie.objects.select_related('director').annotate(num_viewings=Count('viewing')).filter(num_viewings__exact=0, recommended_by__isnull=True).order_by("-id")
    return {'recommended_movies': recommended_movies, 'wish_list': wish_list}
    
@render_to('person_list.html')
def person_list(request):
    movies = Movie.objects.exclude(director__isnull=True).select_related('director').order_by('-director')
    return {'movies': movies}
   
@render_to()
def movie_search(request):

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
                result['thumb'] = get_movie_thumbnail(result)
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
            people = Person.objects.filter(reduce(lambda x, y: x & y, queries)).annotate(num_movies=Count('movie'))
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
