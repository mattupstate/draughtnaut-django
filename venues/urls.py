# This also imports the include function
from django.conf.urls.defaults import patterns

urlpatterns = patterns('venues.views',
    # '/'
    (r'^$', 'venue_list'),
    # '/search/json/'
    (r'^search/json/$', 'search_json'),
    # '/types/'
    (r'^types/$', 'type_list'),
    # '/<id_or_slug>/'
    (r'^(?P<id_or_slug>[\w-]+)/$', 'venue_detail'),
    # '/types/<id_or_slug>'
    (r'^types/(?P<id_or_slug>[\w-]+)/$', 'type_detail'),
)