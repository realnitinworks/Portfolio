from django.urls import path

from .views import post_list, post_detail, post_share_by_email


app_name = "blog"


urlpatterns = [
    path("", post_list, name="post_list"),
    path("<int:year>/<int:month>/<int:day>/<slug:slug>/", post_detail, name="post_detail"),
    path("<int:post_id>/share/", post_share_by_email, name="post_share_by_email")
]
