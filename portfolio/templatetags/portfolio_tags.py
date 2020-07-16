from django import template

from ..quotes import get_random_quote


register = template.Library()


@register.inclusion_tag("portfolio/quotes/quote.html")
def quote():
    return {"quote": get_random_quote()}
