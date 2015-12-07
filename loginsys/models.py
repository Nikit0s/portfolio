from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class AccountManager(BaseUserManager):
	def create_user(self, email, password=None, **kwargs):
		if not email:
			raise ValueError('User must have a valid email address.')
		if not kwargs.get('username'):
			raise ValueError('User must have a valid username.')

		account = self.model(
			email=self.normalize_email(email), username=kwargs.get('username')
		)

		account.set_password(password)
		account.save()

		return account

	def create_superuser(self, email, password, **kwargs):
		account = self.create_user(email, password, **kwargs)

		account.is_admin = True
		account.is_staff = True
		account.is_superuser = True
		account.save()

		return account

class Account(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique=True)
	username = models.CharField(max_length=50, unique=True)

	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	first_name = models.CharField(max_length=50, blank=True, null=True)
	last_name = models.CharField(max_length=50, blank=True, null=True)

	objects = AccountManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email', ]

	def __str__(self):
		return self.email

	def get_full_name(self):
		return ' '.join([self.first_name, self.last_name])

	def get_short_name(self):
		return self.first_name

	def refresh(obj):
		""" Reload an object from the database """
		return obj.__class__._default_manager.get(pk=obj.pk)