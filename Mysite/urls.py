from django.conf.urls import url 

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from MyBlog.views import *
 

urlpatterns = [ 

    url(r'^admin/', (admin.site.urls)),
    url(r'^MyBlog/$', archive),
]