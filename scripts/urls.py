from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.scripts, name='scripts'),
    url(r'^new$', views.newScript, name='newScript'),
    url(r'^new/$', views.newScript, name='newScript'),
]
