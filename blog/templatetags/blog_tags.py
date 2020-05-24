from django import template
from django.utils.safestring import mark_safe

import mistune
from mistune.directives import DirectiveToc
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html


register = template.Library()


class HighlightRenderer(mistune.HTMLRenderer):
    def block_code(self, code, lang=None):
        if lang:
            lexer = get_lexer_by_name(lang, stripall=True)
            formatter = html.HtmlFormatter()
            return highlight(code, lexer, formatter)
        return f'<pre><code>{mistune.escape(code)}</code></pre>'


@register.filter(name="markdown")
def markdown_format(text):
    plugins = [DirectiveToc(), 'url', 'footnotes']
    renderer = HighlightRenderer()
    markdown = mistune.create_markdown(renderer=renderer, plugins=plugins)
    return mark_safe(markdown(text))
