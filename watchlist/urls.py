from django.conf.urls.defaults import *
from watchlist.models import *

urlpatterns = patterns('watchlist.views',
    url(r'^movie/$', 'movie_list', name="movie_list"),
    url(r'^movie/wishlist$', 'wish_list', name="wish_list"),
    url(r'^movie/search$', 'movie_search', name="movie_search"),
    url(r'^movie/tmdb_id/(?P<tmdb_id>[0-9]*)$', 'movie_detail_by_id', name="movie_detail_by_id"),
    # url(r'^movie/import$', 'movie_import', name="movie_import"),
    url(r'^movie/(?P<title>.*)$', 'movie_detail', name="movie_detail"),
    
    url(r'^person/$', 'person_list', name="person_list"),
    url(r'^person/search$', 'person_search', name="person_search"),
    url(r'^person/(?P<name>.*)$', 'person_detail', name="person_detail"),
    
                       
    url(r'^$', 'index', name="movies_index"),
)

urlpatterns += patterns('django.views.generic',
    url(r'^credits.php$', 'simple.direct_to_template', {'template': 'credits.html'}, name="credits"),
                        
)

