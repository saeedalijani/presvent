from django import forms

from Event.models import Presentation, SessionComment, PresentationComment


class PresentationForm(forms.ModelForm):
    class Meta:
        model = Presentation
        exclude = ['user', 'session', 'is_verified']

    def __init__(self, *args, **kwargs):
        super(PresentationForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget = forms.Textarea()
        self.fields['equipment'].widget = forms.Textarea()


class SessionCommentForm(forms.ModelForm):
    class Meta:
        model = SessionComment
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super(SessionCommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget = forms.Textarea()


class PresentationCommentForm(forms.ModelForm):
    class Meta:
        model = PresentationComment
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super(PresentationCommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget = forms.Textarea()
