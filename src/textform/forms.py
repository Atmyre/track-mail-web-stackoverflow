from .models import Message
from comments.models import Comment
from django import forms
import datetime

class IndexForm(forms.Form):
    search = forms.CharField(required=False)

    SORT_CHOICES = (('title', 'post title'), ('author', 'post author'), ('-pub_date', 'publication date'))
    sort = forms.ChoiceField(choices=SORT_CHOICES, label='Sort parameter', initial='author', widget=forms.Select(), required=False)


