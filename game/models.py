from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# print(help(models))

class Play(models.Model):
    player = models.ForeignKey(User, on_delete = models.CASCADE)
    score = models.IntegerField()

