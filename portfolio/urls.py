from django.urls import path

from .views import home, feed

app_name = "portfolio"


urlpatterns = [path("", home, name="home"), path("feeds/", feed, name="feeds")]
