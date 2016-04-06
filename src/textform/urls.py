from django.conf.urls import url, include
from . import views
import comments.views
import comments.urls

app_name = 'textform'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^deletemessage/(?P<pk>[0-9]+)$', views.deletemessage, name='deletemessage'),
    url(r'^editmessage/(?P<pk>.+)$', views.EditMessageView.as_view(), name='editmessage'),
    url(r'^newmessage$', views.NewMessageView.as_view(), name='newmessage'),
    url(r'^(?P<pk>[0-9]+)$', views.MessageView.as_view(), name='detail'),
    url(r'^comments/', include('comments.urls', namespace="comments")),
    url(r'^blogs/', include('blogs.urls', namespace="blogs")),
    url(r'^upmessage/$', views.upmessage, name="upmessage"),
]
