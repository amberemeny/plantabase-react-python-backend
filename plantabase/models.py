from django.db import models
from django.conf import settings


type_choices = (
    ('WATERING', 'Watering'),
    ('FERTILIZING', 'Fertilizing'),
    ('PESTCONTROL', 'Pest Control'),
)

growth_choices = (
    ('SPROUT', 'Sprout'),
    ('SEEDLING', 'Seedling'),
    ('JUVINILLE', 'Juvinille'),
    ('MATURE', 'Mature'),
    ('ESTABLISHED', 'Established'),
)

class Plant(models.Model):
    name = models.CharField(max_length=70)
    species = models.CharField(max_length=70)
    location = models.CharField(max_length=50)
    purchasedate = models.DateField()
    purchaseloc = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    growthstage = models.CharField(max_length=20, choices=growth_choices)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, related_name='plants')

class Schedule(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, null=True, related_name='schedules')
    type = models.CharField(max_length=20, choices=type_choices)
    startdate = models.DateField()
    enddate = models.DateField()
    interval = models.IntegerField()

class Task(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, null=True, related_name='tasks')
    date = models.DateField()
    time = models.TimeField()
    completed = models.BooleanField(default=False)

class Observation(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, null=True, related_name='observations')
    type = models.CharField(max_length=50)
    comment = models.TextField(max_length=200)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)


