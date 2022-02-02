from django.db import models


class Track(models.Model):
    name = models.CharField(max_length=40, default='Track')


class Intake(models.Model):
    name = models.CharField(max_length=40, default='Intake')


class Trainee(models.Model):
    name = models.CharField(max_length=40)
    track_name = models.ForeignKey(Track, on_delete=models.CASCADE)
    intake_name = models.ForeignKey(Intake, on_delete=models.CASCADE)



