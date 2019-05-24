from django.db import models


class Category(models.Model):
    description = models.CharField(max_length=15)


class Event(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    place = models.CharField(max_length=60)
    address = models.CharField(max_length=100)
    initial_date = models.DateField()
    end_date = models.DateField()
    is_on_site = models.BooleanField()
