from django.conf.urls import url
from . import views

app_name = 'comments'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/ajax/$', views.CommentsAjax.as_view(), name='comments_ajax'),
]
