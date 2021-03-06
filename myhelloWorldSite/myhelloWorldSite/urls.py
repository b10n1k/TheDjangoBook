from django.conf.urls import patterns, include, url
from myhelloWorldSite.views import hello, current_datetime, hours_ahead, contact
from books import views
#from contact.forms import Con
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
(r'^admin/',include(admin.site.urls)),
('^hello/$',hello),
('^time/$', current_datetime),
('^time/plus/(\d{1,2})/$',hours_ahead),
#(r'^search_form/$',views.search_form),
(r'^search/$',views.search),
('^contact/$',contact),
)
