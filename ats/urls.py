from django.conf.urls import patterns, url
from . import viewsets

urlpatterns = patterns('',
    url(r'^views/(?P<data_cache>.+)/$',
        viewsets.AtsReportViewSet.as_view(),
        name='ats-report'),
)
