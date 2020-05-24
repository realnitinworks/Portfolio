import os
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Post
from .forms import PostEmailForm
from django.core.mail import send_mail


def post_list(request):
    all_posts = Post.published.all()
    paginator = Paginator(all_posts, os.environ.get("POSTS_PER_PAGE", 3))
    page_number = request.GET.get("page")  # query string in url

    try:
        posts = paginator.page(number=page_number)
    except PageNotAnInteger:
        posts = paginator.page(number=1)  # first page
    except EmptyPage:
        posts = paginator.page(number=paginator.num_pages)  # last page

    return render(
        request, "blog/post/post_list.html", {"posts": posts, "active": "blog"}
    )


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(
        Post, publish__year=year, publish__month=month, publish__day=day, slug=slug
    )

    return render(
        request, "blog/post/post_detail.html", {"post": post, "active": "blog"}
    )


def post_share_by_email(request, post_id):
    post = get_object_or_404(Post, id=post_id, status="published")
    sent = False

    if request.method == "POST":
        form = PostEmailForm(request.POST)
        if form.is_valid():  # Validate and get the cleaned data
            cleaned_data = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cleaned_data['name']} recommends you read " f"{post.title}"
            message = (
                f"Read {post.title} at {post_url}\n\n"
                f"{cleaned_data['name']}'s comments: {cleaned_data['comment']}"
            )
            sender = os.environ.get("EMAIL_SENDER_EMAIL")
            send_mail(subject, message, sender, [cleaned_data["to"]])
            sent = True
    else:
        form = PostEmailForm()

    return render(
        request,
        "blog/post/post_share_email.html",
        {"form": form, "sent": sent, "post": post},
    )
