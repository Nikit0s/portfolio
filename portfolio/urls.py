"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Add an import:  from blog import urls as blog_urls
	2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.http import HttpResponseRedirect
from django.conf.urls.static import static

# urlpatterns = [
# 	# url(r'^auth/', include('loginsys.urls')),
# 	url(r'^admin/', include(admin.site.urls)),
# 	url(r'^gallery/$', include('gallery.urls')),
# 	url(r'^favicon.ico/$', lambda x: HttpResponseRedirect(settings.STATIC_URL+'ico/favicon.ico')), #google chrome favicon fix
# 	url(r'', include('loginsys.urls')),
# ]

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^gallery/', include('gallery.urls')),
	url(r'^registration/$', 'loginsys.views.registration'),
	url(r'^contact/$', 'loginsys.views.contact'),
	url(r'^signin/$', 'loginsys.views.signin'),
	url(r'^visits/$', 'loginsys.views.visitsView'),
	url(r'^visits/(?P<ip>[0-9\.]*)/$', 'loginsys.views.visitsIpView'),
	url(r'^auth/', include('loginsys.urls')),
	url(r'^favicon.ico/$', lambda x: HttpResponseRedirect(settings.STATIC_URL+'ico/favicon.ico')), #google chrome favicon fix
	url(r'^$', include('loginsys.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
