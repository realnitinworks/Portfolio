import os

from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, redirect, render
from taggit.models import Tag

from .forms import PostCommentForm, PostEmailForm
from .models import Post


def post_list(request, tag_slug=None):
    all_posts = Post.published.all()

    tag = None
    if tag_slug:
        # Filter posts based on tag_slug input
        tag = get_object_or_404(Tag, slug=tag_slug)
        all_posts = all_posts.filter(tags__in=[tag])

    paginator = Paginator(all_posts, os.environ.get("POSTS_PER_PAGE", 3))
    page_number = request.GET.get("page")  # query string in url

    try:
        posts = paginator.page(number=page_number)
    except PageNotAnInteger:
        posts = paginator.page(number=1)  # first page
    except EmptyPage:
        posts = paginator.page(number=paginator.num_pages)  # last page

    return render(
        request,
        "blog/post/post_list.html",
        {"all_posts": all_posts, "posts": posts, "active": "blog", "tag": tag},
    )


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(
        Post, publish__year=year, publish__month=month, publish__day=day, slug=slug
    )

    if request.method == "POST":
        form = PostCommentForm(request.POST)
        if form.is_valid():
            # Create 'Comment' model instance backing the form
            # but don't write to DB until for comment-post association
            new_comment = form.save(commit=False)
            # Associate post to the comment
            new_comment.post = post
            # Save to DB
            new_comment.save()
            # Message on successful submit
            messages.add_message(request, messages.SUCCESS, "Your comment is submitted")
            # Redirect to this view
            return redirect(to=post)
    else:
        form = PostCommentForm()

    # Get all the active comments of this post
    all_comments = post.comments.filter(active=True)
    comments_paginator = Paginator(all_comments, os.environ.get("COMMENTS_PER_PAGE", 6))
    comments_page_number = request.GET.get("page")  # query string in url

    try:
        comments = comments_paginator.page(number=comments_page_number)
    except PageNotAnInteger:
        comments = comments_paginator.page(number=1)
    except EmptyPage:
        comments = comments_paginator.page(number=comments_paginator.num_pages)

    return render(
        request,
        "blog/post/post_detail.html",
        {"post": post, "active": "blog", "comments": comments, "form": form},
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
        {"form": form, "sent": sent, "post": post, "active": "blog"},
    )
