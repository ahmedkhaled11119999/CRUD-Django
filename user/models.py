from django.db import models


class MyUser(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=50)
