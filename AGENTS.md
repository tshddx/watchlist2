# AGENTS.md

A personal movie-watchlist site. Django 1.x app backed by themoviedb.org (TMDB) for metadata.

## Critical context: this is Python 2 / Django 1.x code

Do not assume modern Python or Django conventions. Verify with the file before changing it.

- `print` statements (not `print()`), `import tmdb` style (no `watchlist2.` prefix).
- `manage.py` uses `execute_manager(settings)` — removed in Django 1.4+. Pinning matters; `requirements.txt` has no versions and will resolve to incompatible modern releases on Python 3.
- `urls.py` uses `from django.conf.urls.defaults import *` and `patterns(...)` — gone in Django 1.10+.
- `tests.py` uses `failUnlessEqual` — removed in Python 3.12.
- Migrations are **South** (`watchlist/migrations/0001_initial.py` imports `from south.db import db`), not Django's built-in migrations. Do not run `makemigrations` / `migrate` — use South's `schemamigration` / `migrate` if reviving the project.

If asked to "make it run," expect a non-trivial port (Python 2→3, Django 1.2-ish → modern, South → Django migrations, TMDB v2.1 → v3 API). Confirm intent before doing partial fixes that won't actually boot.

## Layout

Flat layout; **`settings.py` and `manage.py` live at the repo root**, not in a `watchlist2/` package. `manage.py` does `import settings` (top-level), so cwd matters.

- `settings.py` — dev (`DEBUG=True`, sqlite3 `db.sqlite3`, hardcoded `SECRET_KEY`).
- `production_settings.py` — just `from settings import *; DEBUG = False`.
- `urls.py` — root URLConf; mounts `watchlist.urls` at `/`.
- `watchlist/` — the only app. Models: `Movie`, `Viewing`, `Person`. Views render to `watchlist/templates/`.
- `tmdb.py`, `tmdb_person.py`, `tmdb_search.py` — vendored TMDB v2.1 XML API client. **API key is hardcoded** in `tmdb.py`; the v2.1 endpoint is long-deprecated (TMDB is on v3 JSON), so live calls likely fail.
- `scripts/` — one-off data-import scripts (`import_csv.py`, `imported_films_12_24_2010.py`). Run via `./manage.py runscript <name>` (django-extensions); they expect cwd = repo root because they read `scripts/films.csv`.
- `watchlist/fixtures/` — JSON fixtures + a backup dir (`2012_04_29_backup/`).
- `site_media/` — served at `/site_media/` by the dev URLConf via `django.views.static.serve`.

## Commands

Standard Django; nothing custom is wired up (no Makefile, no `tox`, no CI).

```
./manage.py runserver         # dev server
./manage.py syncdb            # initial tables (pre-migration apps)
./manage.py migrate            # South migrations for `watchlist`
./manage.py test watchlist     # only stub tests exist (tests.py)
./manage.py runscript <name>   # run scripts/<name>.py (django-extensions)
```

`Procfile` says `python watchlist2/manage.py …` — that path is wrong for the current layout (legacy from a renamed dir). Do not trust it; use `./manage.py` from the repo root.

## Conventions worth knowing

- `Movie.movie_from_tmdb_id` and `Person.person_from_tmdb_id` are the canonical creation paths — they hit TMDB and `get_or_create` by `tmdb_id`. Do not bypass them when adding records; other code assumes TMDB-sourced fields are populated.
- Views/templates rely on model methods like `as_a`, `as_abbreviated_a`, `wrap_in_a` that emit raw HTML strings. Keep them returning strings, not `mark_safe` wrappers, unless you also update templates.
- `urls.py` patterns capture movie/person by **title/name**, not pk (e.g. `r'^movie/(?P<title>.*)$'`). Routes are order-sensitive: `wishlist`, `search`, `tmdb_id/...` must stay above the catch-all.

## Tests

`watchlist/tests.py` is the unmodified Django startapp stub. There is no real test suite to preserve — feel free to replace it.

## What to ask before "fixing" things

- TMDB key is committed in `tmdb.py`; treat as already-public but do not add new secrets to the repo.
- README still points to `ep.io`; git history shows a move to Heroku and then abandonment. Confirm the deployment target before editing deploy files (`Procfile`, `production_settings.py`, `requirements.txt`).
