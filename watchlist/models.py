from django.db import models
from datetime import date

class Movie(models.Model):
    title = models.CharField(max_length=1000)
    release_date = models.DateField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    director = models.ForeignKey('Person', null=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    tmdb_id = models.CharField(max_length=255, null=True, blank=True)
    
    def year(self):
        return self.release_date.year
        
    def most_recent_viewing(self):
        return self.viewing_set.order_by('date')[0].date
        
    def num_viewings(self):
        return self.viewing_set.count()
    
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
    
    def __unicode__(self):
        return self.name
        
    @models.permalink
    def get_absolute_url(self):
        return ('person_detail', (), {'name': self.name})
