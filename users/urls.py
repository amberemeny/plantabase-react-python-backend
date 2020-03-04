from django.urls import include, path
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'', views.UserViewSet, basename='user')

urlpatterns = router.urls