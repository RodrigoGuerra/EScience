from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.files, name='files'),
    url(r'^new$', views.newFile, name='newfile'),
    url(r'^new/$', views.newFile, name='newfile'),
    url(r'^new/InsertFile$', views.insertFile, name='newfile'),
    url(r'^new/UploadFile/(?P<file_id>\w+)$', views.uploadFile, name='newfile'),
    url(r'^(?P<file_id>[0-9|\w]+)/$', views.fileDetails, name='users'),

]
