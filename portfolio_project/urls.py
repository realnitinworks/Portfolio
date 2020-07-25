"""portfolio_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from blog.sitemaps import PostSiteMap

sitemaps = {
    "blog-posts": PostSiteMap,
}

PROJECT_ADMIN_URL = os.environ.get("PROJECT_ADMIN_URL", "admin/")

urlpatterns = [
    path(PROJECT_ADMIN_URL, admin.site.urls),
    path("", include("portfolio.urls", namespace="portfolio")),
    path("blog/", include("blog.urls", namespace="blog")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]

# Using the django-haystack search only for development for now.
if settings.DEBUG:
    urlpatterns += [path("search/", include("haystack.urls"))]
