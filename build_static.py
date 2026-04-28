#!/usr/bin/env python3
"""
Build a static-HTML archive of the Django watchlist site.

Reads the JSON fixtures and the Django templates, then writes one HTML page
per URL route to static_site/. Internal links between pages are relative.
The 'site_media/' directory (CSS/JS/images) was copied verbatim before this
script runs; jQuery 1.4.2 and jQuery UI 1.8.7 were vendored into
static_site/site_media/js/vendor/.

The original site rendered different UI for authenticated vs anonymous users.
We render the anonymous view (the public face of the site).
"""

import json
import os
import re
from collections import defaultdict
from datetime import date

REPO = os.path.dirname(os.path.abspath(__file__))
FIX = os.path.join(REPO, "watchlist", "fixtures")
OUT = os.path.join(REPO, "static_site")


# --------------------------------------------------------------------------
# Slugify (filenames + picsum seeds)

def slugify(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    return s or "untitled"


# --------------------------------------------------------------------------
# Picsum URLs (deterministic per-subject seeds)

def movie_poster(movie):
    return f"https://picsum.photos/seed/movie-{slugify(movie['title'])}/185/278"

def search_thumb(title, idx):
    return f"https://picsum.photos/seed/search-{slugify(title)}-{idx}/185/278"

def person_headshot(person):
    return f"https://picsum.photos/seed/person-{slugify(person['name'])}/120/180"


# --------------------------------------------------------------------------
# Load fixtures

def load_fixtures():
    with open(os.path.join(FIX, "movie_imported_films_12_24_2010.json")) as f:
        movie_rows = json.load(f)
    with open(os.path.join(FIX, "person_imported_films_12_24_2010.json")) as f:
        person_rows = json.load(f)
    with open(os.path.join(FIX, "viewing_imported_films_12_24_2010.json")) as f:
        viewing_rows = json.load(f)

    people = {}
    for row in person_rows:
        pk = row["pk"]
        f = row["fields"]
        people[pk] = {"pk": pk, "name": f["name"], "tmdb_id": f.get("tmdb_id")}

    movies = {}
    for row in movie_rows:
        pk = row["pk"]
        f = row["fields"]
        rd = f.get("release_date")
        year = int(rd[0:4]) if rd else None
        movies[pk] = {
            "pk": pk,
            "title": f["title"],
            "release_date": rd,
            "year": year,
            "runtime": f.get("runtime"),
            "nationality": f.get("nationality"),
            "comments": f.get("comments"),
            "tmdb_id": f.get("tmdb_id"),
            "recommended_by": f.get("recommended_by"),
            "recommend_comments": f.get("recommend_comments"),
            "director_pk": f.get("director"),
        }

    viewings = []
    for row in viewing_rows:
        f = row["fields"]
        viewings.append({
            "pk": row["pk"],
            "date": f["date"],
            "notes": f.get("notes"),
            "movie_pk": f["movie"],
        })

    # Attach computed fields
    movie_viewings = defaultdict(list)
    for v in viewings:
        movie_viewings[v["movie_pk"]].append(v)
    for pk, m in movies.items():
        vs = sorted(movie_viewings[pk], key=lambda x: x["date"], reverse=True)
        m["viewings"] = vs
        m["num_viewings"] = len(vs)
        m["most_recent_viewing"] = vs[0]["date"] if vs else None
        m["director"] = people.get(m["director_pk"])

    person_movies = defaultdict(list)
    for m in movies.values():
        if m["director_pk"]:
            person_movies[m["director_pk"]].append(m)
    for pk, p in people.items():
        ms = sorted(person_movies[pk], key=lambda m: -m["pk"])
        p["movies"] = ms
        p["num_movies"] = len(ms)

    return movies, people, viewings


# --------------------------------------------------------------------------
# HTML helpers

def esc(s):
    if s is None:
        return ""
    return (str(s)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;"))


def media_prefix(depth):
    """Relative path back to static_site/site_media/ from a page at <depth>."""
    return ("../" * depth) + "site_media/"


def page_prefix(depth):
    """Relative path back to static_site/ root from a page at <depth>."""
    return "../" * depth


def short_title(title):
    if len(title) <= 30:
        return title
    return f"{title[:12]} ... {title[-12:]}"


def short_name(name):
    if len(name) >= 20:
        parts = name.split()
        return f"{name[0]}. {parts[-1]}" if parts else name
    return name


def movie_href(depth):
    """All movie detail links land on the same page."""
    return page_prefix(depth) + "movie/detail.html"


def person_href(depth):
    return page_prefix(depth) + "person/detail.html"


def movie_as_a(movie, depth, abbreviated=False):
    """Mirror Movie.as_a / as_abbreviated_a from models.py."""
    if abbreviated and len(movie["title"]) >= 30:
        inner = f'<abbr title="{esc(movie["title"])}"> {esc(short_title(movie["title"]))} </abbr>'
    else:
        inner = esc(movie["title"])
    icon_class = ' class="comments-icon"' if movie.get("comments") else ""
    return f'<a href="{movie_href(depth)}"{icon_class}> {inner} </a>'


def person_as_a(person, depth, abbreviated=False):
    if not person:
        return None
    if abbreviated and len(person["name"]) >= 20:
        inner = f'<abbr title="{esc(person["name"])}"> {esc(short_name(person["name"]))} </abbr>'
    else:
        inner = esc(person["name"])
    return f'<a href="{person_href(depth)}"> {inner} </a>'


# --------------------------------------------------------------------------
# Layout shell (mirrors base.html + base_with_sidebar.html / base_without_sidebar.html)

def layout(title, content_html, depth=0, with_sidebar=True, extra_css="", extra_js=""):
    media = media_prefix(depth)
    root = page_prefix(depth)

    sidebar = ""
    if with_sidebar:
        sidebar = f'''
  <div id="sidebar" class="padded span-4 last push-1">
      <form method="get" action="{root}movie/search-results.html">
        <input type="text" name="query" />
        <input type="submit" value="Search Movie" name="single-movie-search" />
      </form>
      <br />
      <form method="get" action="{root}person/search-results.html">
        <input type="text" name="query" />
        <input type="submit" value="Search Person" name="person-search" />
      </form>
  </div>
'''

    main_span = "span-17" if with_sidebar else "span-23"
    footer_span = "span-17" if with_sidebar else "span-23"

    return f'''<html>
  <head> <title> Movie Watchlist | {esc(title)} </title>

   <link rel="shortcut icon" href="{media}img/favicon.png">

  <link media="screen, projection" type="text/css" href="{media}css/blueprint/screen.css" rel="stylesheet" />
  <link media="print" type="text/css" href="{media}css/blueprint/print.css" rel="stylesheet" />
  <!--[if lt IE 8]><link rel="stylesheet" href="{media}css/blueprint/ie.css" type="text/css" media="screen, projection"><![endif]-->

  <link media="screen, projection" type="text/css" href="{media}css/blueprint_overrides.css" rel="stylesheet" />
  <link media="screen, projection" type="text/css" href="{media}js/jqModal/jqModal.css" rel="stylesheet" />
  <link media="screen, projection" type="text/css" href="{media}js/jqModal/jqModal_overrides.css" rel="stylesheet" />
  <link media="screen, projection" type="text/css" href="{media}css/main.css" rel="stylesheet" />
  <link media="screen, projection" type="text/css" href="{media}css/datepicker.css" rel="stylesheet" />

  {extra_css}

  <script type="text/javascript" src="{media}js/vendor/jquery-1.4.2.min.js"></script>
  <script type="text/javascript" src="{media}js/vendor/jquery-ui-1.8.7.min.js"></script>
  <script type="text/javascript" src="{media}js/jqModal/jqModal.js"></script>
  <script type="text/javascript" src="{media}js/main.js"></script>

  {extra_js}

  </head>

  <body>
    <div class="container">
      <div class="span-10 prepend-top">
        <div id="header">
          <h1><a href="{root}index.html"> Movie Watchlist </a></h1>
        </div>
      </div>
      <div class="span-8 prepend-top last">
        <div id="top-menu">
          <ul>
            <li><a href="{root}movie/index.html"> movies </a>
            <li><a href="{root}person/index.html"> people </a>
            <li><a href="{root}movie/wishlist.html"> todo </a>
          </ul>
        </div>
      </div>

  <div id="main-content" class="padded {main_span}">
{content_html}
  </div>
{sidebar}
  <div id="footer" class="padded {footer_span} last append-top">
    <p class="footer-line">by <a href="http://www.tshaddox.com/?page_id=2">Thomas Shaddox</a>. <a href="{root}credits.html">Credits</a>.</p>
  </div>

    </div>
  </body>

</html>
'''


# --------------------------------------------------------------------------
# Page content builders

def render_index(movies, people, viewings, depth=0):
    # Recent viewings: 10 most recent
    recent = sorted(viewings, key=lambda v: v["date"], reverse=True)[:10]

    # Favorite directors: top 5 by num_movies
    fav = sorted(people.values(), key=lambda p: -p["num_movies"])[:5]

    # Wishlist: movies with 0 viewings, no recommended_by, ordered -id (top 10)
    wishlist = [m for m in movies.values()
                if m["num_viewings"] == 0 and not m["recommended_by"]]
    wishlist.sort(key=lambda m: -m["pk"])
    wishlist = wishlist[:10]

    # Recommended: 0 viewings, recommended_by present
    recommended = [m for m in movies.values()
                   if m["num_viewings"] == 0 and m["recommended_by"]]
    recommended.sort(key=lambda m: -m["pk"])
    recommended = recommended[:9]

    rows_recent = []
    for v in recent:
        m = movies[v["movie_pk"]]
        director_html = person_as_a(m["director"], depth) or "None"
        rows_recent.append(f'''        <tr>
          <td> {movie_as_a(m, depth)} </td>
          <td> {director_html} </td>
          <td> {esc(m["year"])} </td>
          <td> {esc(v["date"])} </td>
          <td> {m["num_viewings"]} </td>
        </tr>''')

    rows_wish = []
    for m in wishlist:
        director_html = person_as_a(m["director"], depth, abbreviated=True) or "None"
        rows_wish.append(f'''          <tr>
            <td> {movie_as_a(m, depth, abbreviated=True)} </td>
            <td> {director_html} </td>
          </tr>''')

    rows_rec = []
    for m in recommended:
        director_html = person_as_a(m["director"], depth, abbreviated=True) or "None"
        rows_rec.append(f'''            <tr>
              <td> {movie_as_a(m, depth, abbreviated=True)} </td>
              <td> {director_html} </td>
            </tr>''')

    rows_dir = []
    for p in fav:
        rows_dir.append(f'''          <tr>
            <td> {person_as_a(p, depth, abbreviated=True)} </td>
            <td> {p["num_movies"]} </td>
          </tr>''')

    if recommended:
        recommended_block = f'''      <table>
        <thead>
          <th>Title</th>
          <th>Director</th>
        </thead>
        <tbody>
{chr(10).join(rows_rec)}
          <tr>
            <td colspan="2"><em>Search for a movie over there to the right to recommend it to me!</em></td>
          </tr>
        </tbody>
      </table>'''
    else:
        recommended_block = "<p>No one has recommended any movies yet. Search for a movie over there to the right to recommend it to me!</p>"

    return f'''  <h2> Recent Viewings </h2>
  <table>
    <thead>
      <th>Title</th>
      <th>Director</th>
      <th>Year</th>
      <th>Watched</th>
      <th>Viewings</th>
    </thead>
    <tbody>
{chr(10).join(rows_recent)}
    </tbody>
  </table>

  <hr />

  <div class="span-8 append-1">
    <h3> Wish List </h3>
    <table>
      <thead>
        <th>Title</th>
        <th>Director</th>
      </thead>
      <tbody>
{chr(10).join(rows_wish)}
      </tbody>
    </table>
  </div>
  <div class="span-8 last">
    <h3> Recommended </h3>
{recommended_block}
  </div>
  <hr />
  <div class="span-5 last">
    <h3> Favorite Directors </h3>
    <table>
      <thead>
        <th>Director</th>
        <th>No.</th>
      </thead>
      <tbody>
{chr(10).join(rows_dir)}
      </tbody>
    </table>
  </div>
'''


def render_movie_list(movies, depth=1):
    # Movies with at least one viewing, ordered by -id
    watched = [m for m in movies.values() if m["num_viewings"] > 0]
    watched.sort(key=lambda m: -m["pk"])

    rows = []
    for m in watched:
        director_html = person_as_a(m["director"], depth) or "None"
        # most_recent_viewing as SHORT_DATE_FORMAT - approximate as MM/DD/YYYY
        mrv = m["most_recent_viewing"]
        if mrv:
            y, mo, d = mrv.split("-")
            mrv_str = f"{int(mo):02d}/{int(d):02d}/{y}"
        else:
            mrv_str = ""
        rows.append(f'''            <tr>
              <td> {movie_as_a(m, depth)} </td>
              <td> {director_html} </td>
              <td> {esc(m["year"])} </td>
              <td> {esc(m["nationality"]) or "None"} </td>
              <td> {mrv_str} </td>
              <td> {m["num_viewings"]} </td>
            </tr>''')

    return f'''  <h2> Movies Watched </h2>
    <table id="movie-table">
      <thead>
        <thead>
          <th class="title">Title</th>
          <th class="director">Director</th>
          <th class="year">Year</th>
          <th class="nationality">Nation.</th>
          <th class="watched" title="Date of the most recent viewing.">Date</th>
          <th class="viewings">No.</th>
        </thead>
        <tbody>
{chr(10).join(rows)}
        </tbody>
      </table>
'''


def render_wish_list(movies, depth=1):
    recommended = [m for m in movies.values()
                   if m["num_viewings"] == 0 and m["recommended_by"]]
    recommended.sort(key=lambda m: -m["pk"])
    recommended = recommended[:10]

    wishlist = [m for m in movies.values()
                if m["num_viewings"] == 0 and not m["recommended_by"]]
    wishlist.sort(key=lambda m: -m["pk"])

    parts = []

    if recommended:
        rrows = []
        for m in recommended:
            director_html = person_as_a(m["director"], depth) or ""
            rrows.append(f'''          <tr>
            <td> {movie_as_a(m, depth)}</a> </td>
            <td> {director_html}</a> </td>
            <td> {esc(m["year"])} </td>
            <td> {esc(m["recommended_by"])} </td>
          </tr>''')
        parts.append(f'''  <h2> Recommended Movies </h2>
    <table>
      <thead>
        <th>Title</th>
        <th>Director</th>
        <th>Year</th>
        <th>Rec. By</th>
      </thead>
      <tbody>
{chr(10).join(rrows)}
      </tbody>
    </table>''')

    if wishlist:
        wrows = []
        for m in wishlist:
            director_html = person_as_a(m["director"], depth) or ""
            wrows.append(f'''          <tr>
            <td> {movie_as_a(m, depth)}</a> </td>
            <td> {director_html}</a> </td>
            <td> {esc(m["year"])} </td>
          </tr>''')
        parts.append(f'''  <h2> Wish List </h2>
    <table>
      <thead>
        <th>Title</th>
        <th>Director</th>
        <th>Year</th>
      </thead>
      <tbody>
{chr(10).join(wrows)}
      </tbody>
    </table>''')

    if not parts:
        parts.append("<p>There are no movies to watch. :(</p>")

    return "\n".join(parts) + "\n"


def render_movie_detail(movie, depth=1):
    """Render the canonical movie detail page. Anonymous user view."""
    poster = movie_poster(movie)
    rd = movie["release_date"] or ""

    director_html = person_as_a(movie["director"], depth) or "None"

    tmdb_html = ""
    if movie["tmdb_id"]:
        tmdb_html = f'''      <dt>tmdb.org</dt>
      <dd><a href="http://www.themoviedb.org/movie/{esc(movie["tmdb_id"])}">{esc(movie["tmdb_id"])}</a></dd>'''

    # Don't actually have an imdb_id at static-build time; omit.

    if movie["viewings"]:
        vrows = []
        for v in movie["viewings"]:
            vrows.append(f'''            <tr>
              <td> {esc(v["date"])} </td>
              <td> {esc(v["notes"]) or "None"} </td>
            </tr>''')
        viewings_block = f'''      <h3> Viewings by Shaddox </h3>
      <table>
        <thead>
          <th>Date</th>
          <th>Notes</th>
        </thead>
        <tbody>
{chr(10).join(vrows)}
        </tbody>
      </table>'''
        if movie["recommended_by"]:
            viewings_block = f'<p><strong>This movie was previously recommended by {esc(movie["recommended_by"])}.</strong></p>\n' + viewings_block
    else:
        if movie["recommended_by"]:
            connector = ", saying:" if movie["recommend_comments"] else "."
            viewings_block = f'<p><strong>{esc(movie["recommended_by"])} recommends this movie{connector}</strong></p>'
            if movie["recommend_comments"]:
                viewings_block += f'\n<p class="indent">{esc(movie["recommend_comments"])}</p>'
        else:
            viewings_block = "<p><strong>This movie is on Shaddox' wish list.</strong></p>"

    comments_block = ""
    if movie["comments"]:
        comments_block = f'''<div class="comments">
      <h3>Comments from Shaddox</h3>
      <p class="indent">{esc(movie["comments"])}</p>
    </div>'''

    return f'''  <h2> {esc(movie["title"])} </h2>
  <div class="span-5 movie-details">
    <div class="movie-thumbnail">
      <img src="{poster}" alt="{esc(movie["title"])} poster" />
    </div>
    <dl>
      <dt>Released</dt>
      <dd>{esc(rd)}</dd>
      <dt>Director</dt>
      <dd>
        {director_html}
      </dd>
      <dt>Nationality</dt>
      <dd>{esc(movie["nationality"]) or "None"}</dd>
      <dt>Runtime</dt>
      <dd>{esc(movie["runtime"]) or 0} minutes</dd>
{tmdb_html}
    </dl>
  </div>
  <div class="span-12 last">
    <div class="movie-buttons">
    </div>
    <br />
{viewings_block}
{comments_block}
  </div>
'''


def render_person_list(people, depth=1):
    # Sort directors by recency of their movies (-id of latest)
    directors = [p for p in people.values() if p["num_movies"] > 0]
    directors.sort(key=lambda p: -max(m["pk"] for m in p["movies"]))

    rows = []
    for p in directors:
        movies_list = p["movies"][:5]
        link_parts = []
        for m in movies_list:
            link_parts.append(f'<a href="{movie_href(depth)}">{esc(m["title"])} ({m["year"]})</a>')
        joined = ", ".join(link_parts)
        if len(p["movies"]) > 5:
            joined += " <span> and more </span>"
        rows.append(f'''        <tr>
          <td> {person_as_a(p, depth)} </td>
          <td>
              {joined}
          </td>
        </tr>''')

    return f'''  <h2> People </h2>
  <table class="person-list">
    <thead>
      <th class="name">Name</th>
      <th class="directed">Directed</th>
    </thead>
    <tbody>
{chr(10).join(rows)}
    </tbody>
  </table>
'''


def render_person_detail(person, depth=1):
    headshot = person_headshot(person)

    tmdb_html = ""
    if person["tmdb_id"]:
        tmdb_html = f'''      <dt>tmdb.org</dt>
      <dd><a href="http://www.themoviedb.org/person/{esc(person["tmdb_id"])}">{esc(person["tmdb_id"])}</a></dd>'''

    if person["movies"]:
        rows = []
        for m in person["movies"]:
            rows.append(f'''            <tr>
              <td> {movie_as_a(m, depth)} </td>
              <td> {m["num_viewings"]} </td>
            </tr>''')
        movies_block = f'''      <h3>Movies</h3>
      <table>
        <thead>
          <th>Title</th>
          <th>Viewings</th>
        </thead>
        <tbody>
{chr(10).join(rows)}
        </tbody>
      </table>'''
    else:
        movies_block = f'<p> {esc(person["name"])} has no movies in the Watchlist. </p>'

    return f'''  <h2> {esc(person["name"])} </h2>
  <div class="span-5">
    <div class="person-thumbnail">
      <img src="{headshot}" width="120" alt="{esc(person["name"])}" />
    </div>
    <dl>
{tmdb_html}
    </dl>
  </div>
  <div class="span-12 last">
{movies_block}
  </div>
'''


def render_movie_search(depth=1):
    root = page_prefix(depth)
    return f'''    <div class="content">
        <h2> Search </h2>
        <p> Provide a list of movies, one per line, with the year optionally after the title.
        <form action="{root}movie/search-results.html" method="get">
            <textarea name="movies_list" id="movies_list"></textarea><br />
            <input type="submit" value="Submit" />
        </form>
    </div>
'''


def render_movie_search_results(movies, depth=1):
    """Fabricate plausible search results for two queries."""
    # Mix of titles that are in the fixture (in_watchlist=True, link to detail)
    # and ones that aren't (in_watchlist=False, show "Recommend" button).
    queries = [
        ("rushmore", ["Rushmore", "The Royal Tenenbaums", "Moonrise Kingdom"]),
        ("annie hall", ["Annie Hall", "Manhattan", "Hannah and Her Sisters"]),
    ]

    movie_by_title = {m["title"]: m for m in movies.values()}

    sections = []
    for query, titles in queries:
        cards = []
        for i, title in enumerate(titles):
            m = movie_by_title.get(title)
            in_watchlist = m is not None
            year = m["release_date"] if m else "Unknown"
            thumb = search_thumb(title, i)
            position = "last" if i == len(titles) - 1 else "append-1"
            if in_watchlist:
                title_html = f'<p style="font-weight: bold;"><a href="{movie_href(depth)}">{esc(title)}</a></p>'
            else:
                title_html = f'<p style="font-weight: bold;">{esc(title)}</p>'
            # Anonymous user: show "Recommend" button when not in db
            buttons_html = ""
            if not in_watchlist:
                buttons_html = '''<div class="movie-buttons">
              <span>
                <a href="" class="recommend-link small-button">Recommend</a>
              </span>
            </div>'''
            cards.append(f'''        <div class="span-5 {position}">
          <div class="padded result span-4">
            {title_html}
            <p>({esc(year)})</p>
            {buttons_html}
            <div class="thumbnail">
              <img src="{thumb}" alt="{esc(title)} Poster" />
            </div>
          </div>
        </div>''')
        sections.append(f'''  <div class="results span-17 last">
      <h3>Results for "{esc(query)}"</h3>
{chr(10).join(cards)}
    </div>
    <hr />''')

    return f'''  <h2> Search Results </h2>
{chr(10).join(sections)}
'''


def render_person_search_results(people, depth=1):
    """Fabricate plausible person-search results."""
    query = "anderson"
    matches = [p for p in people.values() if "anderson" in p["name"].lower()]
    matches.sort(key=lambda p: -p["num_movies"])
    matches = matches[:5]

    if matches:
        items = []
        for p in matches:
            plural = "" if p["num_movies"] == 1 else "s"
            items.append(f'''<p> <span class="person-name"> {person_as_a(p, depth)} </span> ({p["num_movies"]} movie{plural} in Watchlist)</p>''')
        body = f'<h3>Results for "{esc(query)}"</h3>\n' + "\n".join(items)
    else:
        body = f'<h3><i>No results for "{esc(query)}"</i></h3>'

    return f'''  <h2> Search Results </h2>
    <div class="results span-17 last">
{body}
    </div>
    <hr />
'''


def render_credits(depth=0):
    return '''    <h2> Credits </h2>

    <ul>
      <li> This site was created with <a href="http://djangoproject.com">Django</a>, a web framework written in <a href="http://python.org">Python</a>. </li>
      <li> This site is being hosted by <a href="http://www.ep.io">ep.io</a>, a service that provides instant deployment of Django and other Python web applications. ep.io is currently in beta. On twitter <a href="http://twitter.com/epdotio">@epdotio</a>.</li>
      <li> Movie and cast data is taken with permission from <a href="http://themoviedb.org">themoviedb.org</a>. This site uses the <a href="http://api.themoviedb.org/2.1">TMDd API</a> wrapped in <a href="https://github.com/doganaydin/themoviedb">this Python package</a> as well as some custom modifications.
      <li> This site uses the <a href="http://www.blueprintcss.org/">Blueprint</a> CSS framework with some modifications. </li>
      <li> The javascript library <a href="http://jquery.com/">jQuery</a> is used sparingly. The jQuery plugin <a href="http://tablesorter.com/docs/">tablesorter</a> is used. </li>
      <li> The version control system <a href="http://git-scm.com">git</a> is used to manage the source code for this site. All the code can be found on <a href="https://github.com/baddox/watchlist2">github</a>. </li>
      <li> This site was developed mostly using the <a href="http://www.gnu.org/software/emacs/">GNU Emacs</a> text editor running on <a href="http://www.ubuntu.com/">Ubuntu</a>. </li>
      <li> The development of this site would be more annoying were it not for <a href="https://github.com/django-extensions/django-extensions">django-extensions</a>, <a href="https://bitbucket.org/offline/django-annoying/wiki/Home">django-annoying</a>, and <a href="http://south.aeracode.org/">south</a>. </li>
      <li> Also crucial to development of this site is <a href="http://getfirebug.com/">Firebug</a> and the <a href="http://code.google.com/chrome/devtools/">Chrome Developer Tools</a>. </li>
      <li> Color ideas come from  <a href="http://www.colourlovers.com/">ColourLovers</a>. Color manipulation is done with <a href="http://www.iconico.com/colorpic/">ColorPic</a>. </li>
      <li> The best reference for CSS selectors at a glance is the <a href="http://www.css3.info/selectors-test/">CSS3 Selectors Test</a>. <a href="http://css3please.com/"> CSS3 Please!</a> is great for fancy effects.</li>
    </ul>
'''


# --------------------------------------------------------------------------
# Build

def write(path, html):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full) or ".", exist_ok=True)
    with open(full, "w") as f:
        f.write(html)
    print(f"  wrote {path}")


def main():
    movies, people, viewings = load_fixtures()
    print(f"Loaded {len(movies)} movies, {len(people)} people, {len(viewings)} viewings")

    media_root = media_prefix(0)
    media_sub = media_prefix(1)

    # Pick canonical movie + person for the detail pages.
    # Rushmore (pk 1, dir Wes Anderson, has a viewing) is a great showcase.
    canonical_movie = movies[1]
    canonical_person = people[1]  # Wes Anderson
    print(f"Canonical movie: {canonical_movie['title']}")
    print(f"Canonical person: {canonical_person['name']}")

    # 1. /  -> index.html
    write("index.html", layout(
        title="Home",
        content_html=render_index(movies, people, viewings, depth=0),
        depth=0,
        with_sidebar=True,
    ))

    # 2. /movie/  -> movie/index.html  (with tablesorter)
    list_extra_css = f'<link media="screen, projection" type="text/css" href="{media_sub}css/movie_list.css" rel="stylesheet">'
    list_extra_js = f'<script type="text/javascript" src="{media_sub}js/tablesorter/jquery.tablesorter.js"></script>\n  <script type="text/javascript" src="{media_sub}js/movie_list.js"></script>'
    write("movie/index.html", layout(
        title="All Movies",
        content_html=render_movie_list(movies, depth=1),
        depth=1,
        with_sidebar=False,
        extra_css=list_extra_css,
        extra_js=list_extra_js,
    ))

    # 3. /movie/wishlist  -> movie/wishlist.html
    write("movie/wishlist.html", layout(
        title="Movies To Watch",
        content_html=render_wish_list(movies, depth=1),
        depth=1,
        with_sidebar=True,
    ))

    # 4. /movie/search (GET form)
    search_extra_css = f'<link media="screen, projection" type="text/css" href="{media_sub}css/movie_list.css" rel="stylesheet">'
    write("movie/search.html", layout(
        title="All Movies",
        content_html=render_movie_search(depth=1),
        depth=1,
        with_sidebar=True,
        extra_css=search_extra_css,
    ))

    # 5. /movie/search (POST results)
    write("movie/search-results.html", layout(
        title="Search Results",
        content_html=render_movie_search_results(movies, depth=1),
        depth=1,
        with_sidebar=True,
        extra_css=search_extra_css,
    ))

    # 6. /movie/<title>  -> movie/detail.html (Rushmore)
    detail_extra_css = f'<link media="screen, projection" type="text/css" href="{media_sub}css/movie_detail.css" rel="stylesheet">'
    detail_extra_js = f'<script type="text/javascript" src="{media_sub}js/movie_detail.js"></script>'
    write("movie/detail.html", layout(
        title=canonical_movie["title"],
        content_html=render_movie_detail(canonical_movie, depth=1),
        depth=1,
        with_sidebar=True,
        extra_css=detail_extra_css,
        extra_js=detail_extra_js,
    ))

    # 7. /person/  -> person/index.html
    person_list_extra_css = f'<link media="screen, projection" type="text/css" href="{media_sub}css/person_list.css" rel="stylesheet">'
    write("person/index.html", layout(
        title="All People",
        content_html=render_person_list(people, depth=1),
        depth=1,
        with_sidebar=True,
        extra_css=person_list_extra_css,
    ))

    # 8. /person/search (POST results)
    person_search_extra_css = f'<link media="screen, projection" type="text/css" href="{media_sub}css/movie_list.css" rel="stylesheet">'
    write("person/search-results.html", layout(
        title="Search Results",
        content_html=render_person_search_results(people, depth=1),
        depth=1,
        with_sidebar=True,
        extra_css=person_search_extra_css,
    ))

    # 9. /person/<name>  -> person/detail.html (Wes Anderson)
    write("person/detail.html", layout(
        title=canonical_person["name"],
        content_html=render_person_detail(canonical_person, depth=1),
        depth=1,
        with_sidebar=True,
    ))

    # 10. /credits.php  -> credits.html
    write("credits.html", layout(
        title="Credits",
        content_html=render_credits(depth=0),
        depth=0,
        with_sidebar=True,
    ))

    print("Done.")


if __name__ == "__main__":
    main()
