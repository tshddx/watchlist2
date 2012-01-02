import csv, os, pprint, datetime
from watchlist.models import *

films_csv = csv.reader(open(os.path.abspath('scripts/films.csv')), delimiter='\t')
films = []
for row in films_csv:
    film = {}
    if row[0].lower() == "kick-ass":
        print "CHANGED KICK ASS"
        film['title'] = 'kick ass 2010'
    elif row[0].lower() == "good morning":
        print "CHANGED Good Morning"
        film['title'] = 'ohayo'
    elif row[0].lower() == 'lights in the dusk':
        print "CHANGED lights in the dusk"
        film['title'] = 'Laitakaupungin valot'
    elif row[0].lower() == 'shadows in paradise':
        print "CHANGED shadows in paradise"
        film['title'] = 'shadows in paradise 1986'
    elif row[0].lower() == "l'argent":
        print "CHANGED l'argent"
        film['title'] = "l'argent 1983"
    elif row[0].lower() == 'greenburg':
        print "CHANGED greenburg"
        film['title'] = 'greenberg'
    else:
        film['title'] = row[0]
    film['director'] = row[1]
    film['year'] = row[2]
    film['nationality'] = row[3]
    film['runtime'] = row[4]
    film['viewing'] = row[5]
    film['comments'] = row[7]
    if not film['title'].lower().startswith('the deca'):
        films.append(film)
    else:
        print "IGNORED a deca film"
print "____________"
print '------------'
print ''

films = films[1:]
#pprint.pprint(films[21:30])

for film in films:
    result = tmdb.search(film['title'])[0]
    print "%s\tid: %s" % (film['title'], result['id'])
    m = Movie.movie_from_tmdb_id(int(result['id']))
    month, day, year = tuple(map(int, film['viewing'].split('/')))
    m.add_viewing(datetime.date(year, month, day))
    if film['nationality']:
        m.nationality = film['nationality']
    if film['comments']:
        m.comments = film['comments']
    m.save()
    print "   Created movies %s\n   viewed on %s" % (m, m.most_recent_viewing())
    print '----------'

print "\nIt is late, but IT IS DONE!"

# problems:
### kick-ass
#kick ass 2010
#ju dou 
#ohayo
#crank 2
### lights in the dusk
#Laitakaupungin valot
#decalogue ep. 1 and 2
#shadows in paradise 1986
#l'argent 1983
