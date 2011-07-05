# This also imports the include function
from django.conf.urls.defaults import patterns

urlpatterns = patterns('users.views',
    # '/profile/'
    (r'^profile/$', 'profile'),
    # '/logout/'
    (r'^logout/$', 'logout_user'),
    # '/login/'
    (r'^login/$', 'login_user'),
    # '/signup/'
    (r'^signup/$', 'signup_user'),
    # '/<id_or_slug>/'
    (r'^(?P<id_or_username>[\w-]+)/$', 'public_profile'),
)