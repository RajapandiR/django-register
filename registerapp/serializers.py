from rest_framework import serializers
from registerapp import models


class RegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.RegisterPage
		fields = [ 'id', 'name', 'email', 'password' ]