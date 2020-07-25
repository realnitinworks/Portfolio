from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    question = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField(widget=ReCaptchaV3)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["captcha"].label = False
