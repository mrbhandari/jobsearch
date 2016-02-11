from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('authdemo.urls')),
    url(r'^', include('hackathon.urls')),
    url(r'^', include('myprofile.urls')),
    # url(r'^openid/(.*)', SessionConsumer()),
)
