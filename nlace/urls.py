from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
#    (r'^usuarios/', include('logueo.urls')),

    url(r'^$', 'logueo.views.home', name='home'),
    # url(r'^nlace/', include('nlace.foo.urls')),
    url(r'^crear/', 'logueo.views.crear', name='crear'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
