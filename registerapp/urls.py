from django.urls import path, include
from rest_framework import routers

from registerapp import api
from registerapp import views

router = routers.DefaultRouter()
router.register('register', api.RegisterViewSet, basename='register')
urlpatterns = [
	path('', include(router.urls)),	
]