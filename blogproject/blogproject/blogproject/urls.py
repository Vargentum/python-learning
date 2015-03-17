from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^blog/', include('posts.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('pages.urls')),
)
