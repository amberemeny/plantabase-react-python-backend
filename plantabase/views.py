from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PlantSerializer, ObservationSerializer, ScheduleSerializer, TaskSerializer
from .models import Plant, Observation, Schedule, Task
from django.http import HttpResponse, Http404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class PlantView(viewsets.ModelViewSet):
    serializer_class = PlantSerializer
    # queryset = Plant.objects.all()
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Plant.objects.filter(user=self.request.user)
        # return self.request.user.accounts.all()

class ObservationView(viewsets.ModelViewSet):
    serializer_class = ObservationSerializer
    # queryset = Observation.objects.all()
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Observation.objects.filter(plant=self.kwargs['plant_pk'])
    # return self.request.user.accounts.all()

class ScheduleView(viewsets.ModelViewSet):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()
    permission_classes = (IsAuthenticated, )

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated, )