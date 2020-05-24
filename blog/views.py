import os
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Post


def post_list(request):
    all_posts = Post.published.all()
    paginator = Paginator(all_posts, os.environ.get('POSTS_PER_PAGE', 3))
    page_number = request.GET.get('page')  # query string in url

    try:
        posts = paginator.page(number=page_number)
    except PageNotAnInteger:
        posts = paginator.page(number=1)  # first page
    except EmptyPage:
        posts = paginator.page(number=paginator.num_pages)  # last page

    return render(
        request,
        "blog/post/post_list.html",
        {"posts": posts, "active": "blog"}
    )


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(
        Post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
        slug=slug
    )

    return render(
        request,
        "blog/post/post_detail.html",
        {"post": post, "active": "blog"}
    )
