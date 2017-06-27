from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.packs, name='packs'),
    url(r'^new$', views.newPack, name='newPack'),
    url(r'^new/$', views.newPack, name='newPack'),
]
