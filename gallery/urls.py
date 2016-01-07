from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^getcomments/', 'gallery.views.getComments'),
	url(r'^addcomment/', 'gallery.views.addComment'),
	url(r'^addlike/', 'gallery.views.addLike'),
	url(r'^getlikes/', 'gallery.views.getLikes'),
	url(r'^', 'gallery.views.main'),
)