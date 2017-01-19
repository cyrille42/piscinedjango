from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Tip(models.Model):
    texte = models.TextField()
    # replace auteur par just un name
    # vote = models.IntegerField(null=False)
    auteur = models.ForeignKey('auth.User')
    date = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return self.username