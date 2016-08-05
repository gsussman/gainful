from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.overview, name='overview'),
    url(r'^students/$', views.students, name='students'),
    url(r'^groups/$', views.groups, name='groups'),
    url(r'^groups/(?P<id>[-\w]+)/$', views.editgroup, name='editgroup'),
    url(r'^scheduler/$', views.scheduler, name='scheduler'),
    url(r'^overview/$', views.overview, name='overview'),
]