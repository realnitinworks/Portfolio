import os

from django.contrib.postgres.search import (SearchQuery, SearchRank,
                                            SearchVector)
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from blog.models import Post


def home(request):
    return render(request, "portfolio/home.html", {"active": "home"})


def feed(request):
    return render(request, "portfolio/feeds.html", {"active": "feeds"})


def search(request):
    query = request.GET.get("q")
    page_number = request.GET.get("page")

    search_vector = (
        SearchVector("title", weight="A")
        + SearchVector("body", weight="A")
        + SearchVector("summary", weight="B")
    )
    search_query = SearchQuery(query)
    posts = (
        Post.published.annotate(rank=SearchRank(search_vector, search_query))
        .filter(rank__gte=0.3)
        .order_by("-rank")
    )

    paginator = Paginator(posts, os.environ.get("SEARCH_RESULTS_PER_PAGE", 6))

    try:
        posts = paginator.page(number=page_number)
    except PageNotAnInteger:
        posts = paginator.page(number=1)  # first page
    except EmptyPage:
        posts = paginator.page(number=paginator.num_pages)  # last page

    return render(
        request,
        "portfolio/search.html",
        {"posts": posts, "active": "home", "query": query},
    )
