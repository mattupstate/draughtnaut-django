# This also imports the include function
from django.conf.urls.defaults import patterns

urlpatterns = patterns('beer.views',
    # '/'
    (r'^$', 'beer_list'),
    # '/add/'
    (r'^add/$', 'beer_add'),
    # '/search/json'
    (r'^search/json/$', 'search_beer_json'),
    # '/styles/'
    (r'^styles/$', 'style_list'),
    # '/styles/search/json'
    (r'^styles/search/json$', 'search_styles_json'),
    # '/<id_or_slug>'
    (r'^(?P<id_or_slug>[\w-]+)/$', 'beer_detail'),
    # '/styles/<id_or_slug>'
    (r'^styles/(?P<id_or_slug>[\w-]+)/$', 'style_detail'),
)