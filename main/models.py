from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=200, unique=True)
    country = models.CharField(max_length=200, null=True)
    age = models.PositiveIntegerField()

    class Meta:
        ordering = ['id']


class Family(models.Model):
    name = models.CharField(max_length=100)
    members = models.IntegerField()

