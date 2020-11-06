from django.conf.urls import patterns, include, url

from sysadmin.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', index),
	url(r'^login/$', index),
	url(r'^dashboard/$', dashboard),
    url(r'^sysadmin/', include('sysadmin.urls')),
    # Examples:
    # url(r'^$', 'budget.views.home', name='home'),
    # url(r'^budget/', include('budget.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

)
