from django import template
from django.db.models import Count, Q
from django.utils.safestring import mark_safe

import mistune
from mistune.directives import DirectiveToc
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html

from ..models import Post


register = template.Library()


class HighlightRenderer(mistune.HTMLRenderer):
    def block_code(self, code, lang=None):
        if lang:
            lexer = get_lexer_by_name(lang, stripall=True)
            formatter = html.HtmlFormatter()
            return highlight(code, lexer, formatter)
        return f"<pre><code>{mistune.escape(code)}</code></pre>"


@register.filter(name="markdown")
def markdown_format(text):
    plugins = [DirectiveToc(), "url", "footnotes"]
    renderer = HighlightRenderer()
    markdown = mistune.create_markdown(renderer=renderer, plugins=plugins)
    return mark_safe(markdown(text))


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag("blog/post/latest_posts.html")
def show_latest_posts(count=3):
    latest_posts = Post.published.all()[:count]
    return {
        "latest_posts": latest_posts,
    }


@register.simple_tag
def get_most_commented_posts(count=3):
    # https://docs.djangoproject.com/en/3.0/topics/db/aggregation/#cheat-sheet
    # We want group posts and order them by the total number of active comments.
    total_active_comments = Count("comments", filter=Q(comments__active=True))
    return (
        Post.published.annotate(total_comments=total_active_comments)
        .order_by("-total_comments")
        .filter(total_comments__gt=0)[:count]
    )


@register.simple_tag
def total_active_comments(post):
    return post.comments.filter(active=True).count()
