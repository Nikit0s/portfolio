from django.db import models
from loginsys.models import Account

# Create your models here.

class Photos(models.Model):
	class Meta():
		db_table = 'Photos'
		verbose_name = 'Photos'
		verbose_name_plural = 'Photos'
	photo = models.ImageField(upload_to='photos');

class Comments(models.Model):
	class Meta():
		db_table = 'Comments'
		verbose_name = 'Comments'
		verbose_name = 'Comments'
	user = models.ForeignKey(Account)
	commentText = models.TextField()
	commentPhoto = models.ForeignKey(Photos)
	timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)