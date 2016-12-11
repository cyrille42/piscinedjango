from django.db import models
from django.utils import timezone
# Create your models here.

class Movies(models.Model):
    title = models.CharField(max_length=64, null=False)
    episode_nb = models.IntegerField(primary_key=True, null=False)
    opening_crawl = models.TextField()
    director = models.CharField(max_length=32, null=False)
    producer = models.CharField(max_length=128, null=False)
    release_date = models.DateField()

    def __str__(self):
        return self.title