from django.conf.urls import patterns

urlpatterns = patterns('',
    (r'^logdata/hem/(?P<curwatts>\d+)', 'api.views.logdata_hem'),
                       )
