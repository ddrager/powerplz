from django.conf.urls import patterns

urlpatterns = patterns('',
    (r'^logdata/hem/(?P<curwatts>\d+)', 'api.views.logdata_hem'), # log hem data
    (r'^logdata/(?P<value>\d+)', 'api.views.logdata'), # echo back the value for testing
)
