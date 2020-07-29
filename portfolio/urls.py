from django.conf import settings
from django.urls import path

from .views import contact, feed, home, portfolio, project_detail, search

app_name = "portfolio"


urlpatterns = [
    path("", home, name="home"),
    path("feeds/", feed, name="feeds"),
    path("contact/", contact, name="contact"),
    path("portfolio/", portfolio, name="portfolio"),
    path("project/<int:id>/<slug:slug>/", project_detail, name="project_detail"),
]

# Use PostgreSQL full-text search engine in production
if not settings.DEBUG:
    urlpatterns += [path("search/", search, name="search")]
