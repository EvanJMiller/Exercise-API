from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Exercise(models.Model):

    EXERCISE_TYPES = [("AR", "aerobic"),
                      ("ST", "Strength"),
                      ("BA", "Balance"),
                      ("FL", "Flexibility")]

    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    type = models.CharField(max_length=20,choices=EXERCISE_TYPES)
    weight = models.FloatField()
    weight_units = models.CharField(max_length=20, choices=[("KG", "Kilograms"), ("LB", "Pounds")])
    sets = models.IntegerField(default=0)
    reps = models.IntegerField(default=0)
    duration = models.TimeField()
    muscle_target = models.CharField(max_length=400)

class WorkOut(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    exercises = models.ManyToManyField(Exercise, name='workouts')
