from django.contrib import admin
from loginsys.models import Account
# Register your models here.

class AccountAdmin(admin.ModelAdmin):
	list_filter = ['username']
	list_display = ['username', 'email']

admin.site.register(Account, AccountAdmin)