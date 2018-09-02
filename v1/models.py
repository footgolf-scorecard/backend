import datetime
from django.contrib.auth.models import User
from django.db import models

class Hole(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, default=None, blank=True)
    number = models.IntegerField(default=0)
    yardage = models.IntegerField(default=0)
    par = models.IntegerField(default=0)

class Course(models.Model):
    name = models.CharField(max_length=50, default='')
    holes = models.ManyToManyField(Hole, related_name='+', blank=True)
    address = models.CharField(max_length=200, default='', blank=True)
    length = models.IntegerField(default=9)

class Score(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE, default=None)
    player = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    hole = models.ForeignKey(Hole, on_delete=models.CASCADE, default=None)
    total = models.IntegerField(default=0)

class Game(models.Model):
    players = models.ManyToManyField(User, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None)
    scores = models.ManyToManyField(Score, related_name='+', blank=True)
    date = models.DateTimeField('date played', default=datetime.date.today)
