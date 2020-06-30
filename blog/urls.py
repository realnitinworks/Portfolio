from django.urls import path, include

from .feeds import PostsFeed
from .views import post_detail, post_list, post_share_by_email

app_name = "blog"


urlpatterns = [
    path("", post_list, name="post_list"),
    path("tag/<slug:tag_slug>/", post_list, name="post_list_by_tag"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:slug>/", post_detail, name="post_detail"
    ),
    path("<int:post_id>/share/", post_share_by_email, name="post_share_by_email"),
    path("feeds/", PostsFeed(), name="posts_feeds"),
    path("feeds/<int:count>/", PostsFeed(), name="latest_posts_feeds"),
    path("search/", include('haystack.urls')),
]
