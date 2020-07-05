from django.conf import settings
from django.urls import path

from .views import feed, home, search

app_name = "portfolio"


urlpatterns = [
    path("", home, name="home"),
    path("feeds/", feed, name="feeds"),
]

# Use PostgreSQL full-text search engine in production
if not settings.DEBUG:
    urlpatterns += [path("search/", search, name="search")]
