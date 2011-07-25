from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from main.views import main_index

# Enable admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', main_index, name='main-index'),
    (r'^beer/', include('beer.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()