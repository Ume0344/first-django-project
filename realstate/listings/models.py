from django.db import models


class Listing(models.Model):
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    total_rooms = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    size = models.CharField(max_length=100)

    def __str__(self):
        return self.title
