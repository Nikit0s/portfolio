from django.contrib import admin
from gallery.models import Comments, Photos

# Register your models here.

class PhotosAdmin(admin.ModelAdmin):
	list_display = ['photo']

class CommentsAdmin(admin.ModelAdmin):
	list_filter = ['timestamp']
	list_display = ['commentText', 'commentPhoto', 'timestamp']

admin.site.register(Comments, CommentsAdmin)
admin.site.register(Photos, PhotosAdmin)