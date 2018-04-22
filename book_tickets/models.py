# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.

class Book(models.Model):
    theatre_name = models.CharField(max_length=200)
    timeslot = models.IntegerField()
    date = models.DateTimeField()
    
    def publish(self):
        self.save()

    def __str__(self):
        return (self.theatre_name, self.timeslot, self.date)
        
    def theatre(self):
        return (self.theatre_name)
        
        
class Theatre(models.Model):
    theatre_name = models.CharField(max_length=200)
	
    def publish(self):
        self.save()

    def __str__(self):
        return (self.theatre_name)
