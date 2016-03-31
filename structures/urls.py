from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^(?P<cat_id>[0-9]+)/$', views.stru, name='stru'),
    url(r'^edit/$', views.add_edit_struc, name='add_edit_struc'),
]
