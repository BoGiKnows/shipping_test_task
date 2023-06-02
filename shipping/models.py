import csv
from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zip = models.PositiveIntegerField(unique=True)
    lon = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return f'{self.city} - {self.zip}'


class Car(models.Model):
    plate = models.CharField(max_length=5, unique=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='car')
    capacity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.plate


class Cargo(models.Model):
    pick_up_loc = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='pick_up')
    delivery_loc = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='delivery')
    capacity = models.PositiveSmallIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.description