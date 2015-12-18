from django.conf.urls import patterns, include, url
from django.contrib import admin
from 題庫.介面 import 練習

urlpatterns = patterns(
    '',
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'練習/$', 練習)
)
