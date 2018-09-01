from django.contrib.auth.models import User
from django.db import models

class Hole(models.Model):
    number: models.IntegerField(default=0)
    yardage: models.IntegerField(default=0)
    par: models.IntegerField(default=0)

class Course(models.Model):
    name: models.CharField(max_length=50)
    holes: models.ManyToManyField(Hole)
    address: models.CharField(max_length=200)

class Score(models.Model):
    player: models.ForeignKey(User, on_delete=models.CASCADE)
    hole: models.ForeignKey(Hole, on_delete=models.CASCADE)
    total: models.IntegerField(default=0)

class Game(models.Model):
    players: models.ManyToManyField(User)
    course: models.ForeignKey(Course, on_delete=models.CASCADE)
    scores: models.ManyToManyField(Score)
    date: models.DateTimeField('date played')
