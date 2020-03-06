from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers

from plantabase import views

router = routers.SimpleRouter()
router.register(r'plants', views.PlantView, 'plants')

plants_router = routers.NestedSimpleRouter(router, r'plants', lookup='plant')
plants_router.register(r'observations', views.ObservationView, 'observations')

router.register(r'schedules', views.ScheduleView, 'schedules')
router.register(r'tasks', views.TaskView, 'tasks')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include(plants_router.urls)),
    path('api/', include('plantabase.urls')),
]