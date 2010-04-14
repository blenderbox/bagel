from django.conf.urls.defaults import *

urlpatterns = patterns('DjangoMPC.babik.views',
    (r'^$', 'index'),
    (r'^playlist/$', 'playlist'),
    (r'^browse/$', 'browse', {'path': False}),
    (r'^browse/(?P<path>[ _\.\!\&\(\)\'\w\/-]+)/$', 'browse'),
    (r'^controller/(?P<action>[a-z_]+)/(?P<songid>\d+)/$', 'controller'),
    (r'^controller/(?P<action>[a-z_]+)/$', 'controller'),
    )

#urlpatterns += patterns('',)
