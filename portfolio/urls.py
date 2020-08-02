from django.conf import settings
from django.urls import path

from . import views

app_name = "portfolio"


urlpatterns = [
    path("", views.home, name="home"),
    path("feeds/", views.feed, name="feeds"),
    path("contact/", views.contact, name="contact"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("project/<int:id>/<slug:slug>/", views.project_detail, name="project_detail"),
    path(
        "certificate/<int:id>/<slug:slug>/",
        views.certificate_group_detail,
        name="certificate_group_detail",
    ),
]

# Use PostgreSQL full-text search engine in production
if not settings.DEBUG:
    urlpatterns += [path("search/", views.search, name="search")]
