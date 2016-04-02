from django.shortcuts import get_object_or_404, render, redirect

from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.utils import timezone
from django.views import generic
from .models import Message, Comment
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from login.models import UserProfile


class CommentsAjax(generic.DetailView):
    template_name = 'comments/comments_ajax.html'
    model = Message
    context_object_name = 'message'
