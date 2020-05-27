from rest_framework import viewsets
from rest_framework.views import APIView

from registerapp import serializers
from registerapp import models

class RegisterViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.RegisterSerializer
	queryset = models.RegisterPage.objects.all()

