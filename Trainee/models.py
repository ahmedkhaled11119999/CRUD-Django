from django.db import models


class Track(models.Model):
    name = models.CharField(max_length=40)


class Trainee(models.Model):
    name = models.CharField(max_length=40)
    track_name = models.ForeignKey(Track, on_delete=models.CASCADE)


