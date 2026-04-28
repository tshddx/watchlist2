# Watchlist — static archive

A static-HTML snapshot of the Django watchlist app, generated from its templates and JSON fixtures. No server required — open `index.html` in a browser.

## Pages

| File | Original Django route |
|---|---|
| `index.html` | `/` |
| `movie/index.html` | `/movie/` (all watched movies) |
| `movie/wishlist.html` | `/movie/wishlist` |
| `movie/search.html` | `/movie/search` (form) |
| `movie/search-results.html` | `/movie/search` (POST results — fabricated for two example queries) |
| `movie/detail.html` | `/movie/<title>` (canonical: Rushmore) |
| `person/index.html` | `/person/` |
| `person/detail.html` | `/person/<name>` (canonical: Wes Anderson) |
| `person/search-results.html` | `/person/search` (POST results — fabricated query "anderson") |
| `credits.html` | `/credits.php` |

All movie titles in tables/lists link to the same `movie/detail.html`; all person names link to the same `person/detail.html`. This is a static archive, not a full clone — there is one canonical detail page per type.

## Notes

- Rendered as an **anonymous visitor** (no auth-only UI like "Just Watched" or "Add to Wish List").
- Forms render but submit-action navigates to the static results page (no real search runs).
- Movie posters and person headshots use `picsum.photos` placeholders, seeded uniquely per movie/person, so each picture is stable and roughly the same dimensions as the original TMDB thumbnails.
- jQuery 1.4.2 and jQuery UI 1.8.7 are vendored under `site_media/js/vendor/` so the page works offline (modulo the picsum images, which need internet).
- Tablesorter on the watched-movies list is functional.

## Regenerating

From the repo root:

    python3 build_static.py

The script reads the JSON fixtures in `watchlist/fixtures/`, the original templates in `watchlist/templates/`, and the assets in `site_media/`, and writes everything under `static_site/`.
