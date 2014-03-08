from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view())
)
