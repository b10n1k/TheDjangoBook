from django.conf.urls import patterns, include, url
from myhelloWorldSite.views import hello, current_datetime, hours_ahead
from books import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
(r'^admin/',include(admin.site.urls)),
('^hello/$',hello),
('^time/$', current_datetime),
('^time/plus/(\d{1,2})/$',hours_ahead),
(r'^search_form/$',views.search_form),
(r'^search/$',views.search),
)
