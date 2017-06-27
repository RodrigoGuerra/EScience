from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.groups, name='groups'),
    url(r'^new$', views.newGroup, name='newGroup'),
    url(r'^new/$', views.newGroup, name='newGroup'),
    url(r'^(?P<group_id>[0-9|\w]+)/$', views.groupDetails, name='groupDetails'),
]
