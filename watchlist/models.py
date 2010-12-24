from django.db import models
import datetime
from themoviedb import tmdb
import tmdb_person

class Movie(models.Model):
    title = models.CharField(max_length=1000)
    release_date = models.DateField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    director = models.ForeignKey('Person', null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    tmdb_id = models.CharField(max_length=255, null=True, blank=True)
    
    def year(self):
        return self.release_date.year if self.release_date else None
        
    def most_recent_viewing(self):
        try:
            return self.viewing_set.order_by('date')[0].date
        except IndexError:
            return None

    def num_viewings(self):
        return self.viewing_set.count()

    def add_viewing(self, date=None):
        if not date:
            self.viewing_set.create(date=datetime.date.today())
        else:
            self.viewing_set.create(date=date)

    @classmethod
    def movie_from_tmdb_id(cls, tmdb_id):
        """Return a Movie object with the specified tmdb_id. As a side effect, create the Movie in
        the database and fill in its info from themoviedb if it doesn't already exist in the database."""
        movie, created = cls.objects.get_or_create(tmdb_id=tmdb_id)
        # if the Movie is already in the db, we won't change it at all, the assumption
        # being that all Movies will be added with this method so info will correct.
        if created:
            result = tmdb.getMovieInfo(tmdb_id)
            movie.title = result['name']
            # date_string is of the format "YYYY-MM-DD"
            date_string = result['released']
            year = int(date_string[0:4])
            month = int(date_string[5:7])
            day = int(date_string[8:10])
            movie.release_date = datetime.date(year, month, day)
            movie.runtime = int(result['runtime'])
            try:
                director_id = int(result['cast']['director'][0]['id'])
                director = Person.person_from_tmdb_id(director_id)
                movie.director = director
            except KeyError:
                pass
            movie.save()
        return movie

    def short_title(self):
        if len(self.title) <= 30:
            return self.title
        else:
            return "%s ... %s" % (self.title[:12], self.title[-12:])

    def as_abbr(self):
        if len(self.title) <= 30:
            return self.title
        else:
            return '<abbr title="%s"> %s </abbr>' % (self.title, self.short_title())
    
    def __unicode__(self):
        return "%s (%s)" % (self.title, self.year())
    
    @models.permalink
    def get_absolute_url(self):
        return ('movie_detail', (), {'title': self.title})
    
class Viewing(models.Model):
    movie = models.ForeignKey(Movie)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    
    def short_date(self):
        return date.strftime("%m/%d/%Y")
    
    def __unicode__(self):
        return '"%s" on %s' % (self.movie.title, self.date.strftime("%b %d, %Y"))
        
    # @models.permalink
    # def get_absolute_url(self):
        # return ('viewing_detail', (), {'pk': self.pk})
        
class Person(models.Model):
    name = models.CharField(max_length=1000)
    tmdb_id = models.CharField(max_length=255, null=True, blank=True)

    @classmethod
    def person_from_tmdb_id(cls, tmdb_id):
        """Return a Person object with the specified tmdb_id. As a side effect, create the Person in
        the database and fill in their name from themoviedb if they don't already exist in the database."""
        person, created = cls.objects.get_or_create(tmdb_id=tmdb_id)
        # if the Person is already in the db, we won't change it at all, the assumption
        # being that all Persons will be added with this method so info will always correct.
        if created:
            result = tmdb_person.getPersonInfo(tmdb_id)
            person.name = result['name']
            person.save()
        return person
    
    def num_movies(self):
        return self.movie_set.count()

    def __unicode__(self):
        return self.name

    def as_a(self):
        return '<a href="%s"> %s </a>' % (self.get_absolute_url(), self.name)
        
    @models.permalink
    def get_absolute_url(self):
        return ('person_detail', (), {'name': self.name})
