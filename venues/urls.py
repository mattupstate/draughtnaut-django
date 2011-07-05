# This also imports the include function
from django.conf.urls.defaults import patterns

urlpatterns = patterns('venues.views',
    # '/'
    (r'^$', 'venue_list'),
    # '/search/json/'
    (r'^search/json/$', 'search_json'),
    # '/beer/add/'
    (r'^beer/add/$', 'add_beer_ontap'),
    # '/beer/remove/'
    (r'^beer/remove/$', 'remove_beer_ontap'),
    # '/types/'
    (r'^types/$', 'type_list'),
    # '/<id_or_slug>/'
    (r'^(?P<id_or_slug>[\w-]+)/$', 'venue_detail'),
    # '/types/<id_or_slug>'
    (r'^types/(?P<id_or_slug>[\w-]+)/$', 'type_detail'),
)