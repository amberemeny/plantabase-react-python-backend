from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from plantabase import views

router = routers.DefaultRouter()
router.register(r'plants', views.PlantView, 'plants')
router.register(r'observations', views.ObservationView, 'observations')
router.register(r'schedules', views.ScheduleView, 'schedules')
router.register(r'tasks', views.TaskView, 'tasks')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('plantabase.urls')),
]