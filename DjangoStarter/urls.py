from django.conf.urls import patterns, include, url
from DjangoStarter.views import *

#The following enables the Django "Admin" view. 
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
     #Django allows us to URLs to functions using Regular Expressions.
     url(r'^$', basic_view),
     url(r'^basic$', basic_view),
     #It is good practice to allow the trailing slash in URLs.
     url(r'^basic/$', basic_view),
     #However, with RegEx the top two URLs can be simplified to:
     url(r'^basic/?$', basic_view),

     #Notice that we can have multiple views point to the same function.
     url(r'^view_with_vars$', view_with_vars),

     #You can also pass variables through the URL.
     url(r'^url_view$', url_view, {"my_url_var":"This is the URL variable!"}),

#    url(r'^admin/', include(admin.site.urls)),
)
