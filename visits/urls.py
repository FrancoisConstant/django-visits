from django.conf.urls import patterns, url

urlpatterns = patterns('visits.views',
    url(r'^visits/add/$', 'count_visit_ajax', name='count-visit-ajax'),
)