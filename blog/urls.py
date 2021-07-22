from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = (
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post.movie_details.movie_director/(?P<pk>[0-9]+)/$', views.movie_director, name='movie_director'),

)
