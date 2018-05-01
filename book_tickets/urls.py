from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^add/$', views.add, name='add'),
    url(r'^search/$', views.search, name='search'),
    url(r'^$', views.post, name='post'),
]