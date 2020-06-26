# https://docs.djangoproject.com/en/3.0/ref/contrib/syndication/

from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from django.urls import reverse_lazy

from .models import Post


class CustomPostsFeedGenerator(Rss201rev2Feed):
    # https://stackoverflow.com/questions/5163637/django-rss-add-attribute-into-item
    # https://www.devinterface.com/en/blog/how-to-create-a-custom-feed-in-django-using-the-syndication-feed-framework
    # https://docs.djangoproject.com/en/3.0/ref/contrib/syndication/#custom-feed-generators
    def add_item_elements(self, handler, item):
        super().add_item_elements(handler, item)
        handler.addQuickElement("publish_date", item['publish_date'])


class PostsFeed(Feed):
    # Important: For adding extra fields to each item feed
    feed_type = CustomPostsFeedGenerator

    title = "RealNitinWorks Blog"
    link = reverse_lazy("blog:post_list")
    description = "A collection of all the posts written on the blog."

    # https://docs.djangoproject.com/en/3.0/ref/contrib/syndication/#a-complex-example
    # Like a view, the arguments in the URL are passed to the get_object() method along with the request object.
    def get_object(self, request, count=None):
        """ Return all posts or 'count' number of posts """
        if not count:
            return Post.published.all()

        # Modify top level description if only a given number of posts are requested.   
        self.description = f"A collection of the {count} latest posts written on the blog."
        return Post.published.all()[:count]

    # https://docs.djangoproject.com/en/3.0/ref/contrib/syndication/#a-complex-example
    def items(self, obj):
        return obj

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.summary

    # Add custom elements to the item feed
    def item_extra_kwargs(self, item):
        return {
            # Add extra element "publish_date" to the item feed
            "publish_date": str(item.publish),
        }
