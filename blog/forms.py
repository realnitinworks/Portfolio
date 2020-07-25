from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from django import forms
from pagedown.widgets import AdminPagedownWidget

from .models import Comment, Post


class PostAdminForm(forms.ModelForm):
    """
    This class is used to render Stack Overflow's "Pagedown" Markdown editor
    to Django Admin for the Post model.

    https://github.com/timmyomahony/django-pagedown
    """

    body = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Post
        fields = "__all__"


class PostEmailForm(forms.Form):
    """
    Form for sharing post by email.
    """

    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comment = forms.CharField(required=False, widget=forms.Textarea)
    captcha = ReCaptchaField(widget=ReCaptchaV3)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["captcha"].label = False


class PostCommentForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV3)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["captcha"].label = False

    class Meta:
        model = Comment
        fields = ("name", "email", "body")
