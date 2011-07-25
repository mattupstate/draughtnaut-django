from django.conf.urls.defaults import patterns, url
from beer import views

urlpatterns = patterns('beer.views',
    # '/'
    url('^$', views.beer_index, name='beer-index'),
    # '/<id>/'
    url('^(?P<id>[\d]+)/$', views.beer_show),
    # '/search/'
    url('^search/$', views.beer_search),
    # '/styles/'
    url('^styles/$', views.styles_index),
    # '/styles/<id>/'
    url('^styles/(?P<id>[\d]+)/$', views.styles_show),
    # '/styles/search'
    url('^styles/search$', views.styles_search),
)