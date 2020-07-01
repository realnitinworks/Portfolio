from haystack import indexes

from .models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    # https://django-haystack.readthedocs.io/en/master/tutorial.html
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Post
