from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Enable admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'home.views.index'),
    (r'^beer/', include('beer.urls')),
    (r'^venues/', include('venues.urls')),
    #(r'^users/login/$', 'django.contrib.auth.views.login', {'template_name': 'users/login.html'}),
    (r'^users/', include('users.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()