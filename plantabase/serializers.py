from rest_framework import serializers

from plantabase.models import Plant, Observation, Schedule, Task

class PlantSerializer(serializers.ModelSerializer):
    observations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    schedules = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta: 
        model = Plant
        fields = ('name', 'species', 'location', 'purchasedate', 'purchaseloc', 'price', 'growthstage', 'observations', 'schedules', 'user', 'id')

class ObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observation
        fields = ('plant', 'type', 'comment', 'date', 'time')

class ScheduleSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Schedule
        fields = ('plant', 'type', 'startdate', 'enddate', 'interval', 'tasks')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('schedule', 'date', 'time', 'completed')