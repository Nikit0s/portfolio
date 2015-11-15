from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'viestats.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	url(r'^contact/$', 'loginsys.views.contact'),
	url(r'^', 'loginsys.views.main'),
)
