from django.conf import settings
from django.urls import path

from .views import contact, feed, home, search

app_name = "portfolio"


urlpatterns = [
    path("", home, name="home"),
    path("feeds/", feed, name="feeds"),
    path("contact/", contact, name="contact"),
]

# Use PostgreSQL full-text search engine in production
if not settings.DEBUG:
    urlpatterns += [path("search/", search, name="search")]
