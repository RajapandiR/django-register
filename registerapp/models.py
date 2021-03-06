from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.conf import settings

# Create your models here.

class RegisterManager(BaseUserManager):

	def create_user(self, email, name, password):
		"""Create a User """
		if not email :
			raise ValueError('User must have an Email Address')

		email = self.normalize_email(email)
		user = self.model(email=email ,name=name)
		# password = make_password(password)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, name, password):

		user = self.create_user(email, name, password)
		user.is_superuser = True
		user.is_staff = True
		user.save(using=self._db)
		return user

class RegisterPage(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(max_length=100, unique= True)
	name = models.CharField(max_length=100)
	is_active = models.BooleanField(default = True)
	is_staff = models.BooleanField(default = False)
	objects = RegisterManager()
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']
	
	def get_full_name(self):
		return self.name

	def __str__(self):
		return self.email