from django.urls import path

from .views import feed, home

app_name = "portfolio"


urlpatterns = [path("", home, name="home"), path("feeds/", feed, name="feeds")]
