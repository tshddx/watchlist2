import tmdb

def tmdb_search(string, num_results=3):
    t = tmdb.MovieDb()
    results = []
    for match in t.search(string)[:num_results]:
        result = {}
        result['title'] = match['name']
        result['year'] = match['released'][:4] if match['released'] else "No year data" # just the year
        result['director'] = 'Not yet implemented.'
        if (match['images']):
            result['poster_thumb'] = match['images'][0]['thumb']
            # result['poster_medium'] = match['images'][0]['cover']
            # result['poster_large'] = match['images'][0]['mid']
        results.append(result)
    return results
