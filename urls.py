from django.conf.urls import patterns, include, url
#from rweb.views import home
from joins.views import home,upload_file
from quiz.views import disp
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',home),
   # url(r'^(?P<ref_id>.*)$',share),   
    url(r'^upload/$',upload_file),
    url(r'^quiz/$',disp),
    
    # Examples:
    # url(r'^$', 'rweb.views.home', name='home'),
    # url(r'^rweb/', include('rweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
)
