from .models import Tag, Message
from django import forms
from django.core.exceptions import ValidationError

class IndexForm(forms.Form):
    search = forms.CharField(required=False)

    SORT_CHOICES = (('title', 'post title'), ('author', 'post author'), ('-pub_date', 'publication date'), ('-comments_count', 'rating'))
    sort = forms.ChoiceField(choices=SORT_CHOICES, label='Sort parameter', initial='author', widget=forms.Select(), required=False)

class MessageForm(forms.ModelForm):
    max_tag_number = 3
    class Meta:
        model = Message
        fields = ('title', 'text', 'blog', 'tags')

    def clean_tags(self):
        tags = self.cleaned_data.get('tags')
        if tags and tags.count() > self.max_tag_number:
            raise ValidationError('Maximum %(self.max_tag_number)s categories are allowed.', code='invalid',)

        return tags


