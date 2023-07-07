from django.db import models
from django.shortcuts import render

# Create your models here.


class News(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.headline
