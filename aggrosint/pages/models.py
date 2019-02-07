from django.db import models

# Create your models here.

from django.db import models


class Operation(models.Model):
    title = models.TextField(max_length=50)
    body = models.TextField()
    name = models.TextField(max_length=75)
    def __str__(self):
        return self.title[:50]

class Intel(models.Model):
    operation = models.CharField(max_length=200)
    title = models.CharField(max_length=25)
    category = models.CharField(max_length=50)
    url = models.URLField()
    reason = models.TextField(max_length=600)
    time = models.TimeField(auto_now=True)
    def __str__(self):
        return self.title[:50]

class Tools(models.Model):
    title = models.TextField(max_length=50)
    url = models.URLField()
    category = models.TextField()

    def __str__(self):
        return self.title[:50]
