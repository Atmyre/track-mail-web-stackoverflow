# coding: utf-8

from .models import UserProfile
from textform.models import Message
from django.contrib.auth.models import User
from django import forms

class BlogForm(forms.Form):
    search = forms.CharField(required=False)

    SORT_CHOICES = (('title', 'post title'), ('author', 'post author'), ('-pub_date', 'publication date'))
    sort = forms.ChoiceField(choices=SORT_CHOICES, label='sort parameter', initial='author', widget=forms.Select(),
                             required=False)
