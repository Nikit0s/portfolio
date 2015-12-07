from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'viestats.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	url(r'^contact/$', 'loginsys.views.contact'),
	url(r'^register/$', 'loginsys.views.register'),
	url(r'^login/$', 'loginsys.views.login'),
	url(r'^logout/$', 'loginsys.views.logout'),
	url(r'^', 'loginsys.views.main'),
)
