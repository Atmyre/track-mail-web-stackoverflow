from django.conf.urls import url

from . import views
from django.views import generic

app_name = 'blogs'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.BlogView.as_view(), name='detail'),
]
