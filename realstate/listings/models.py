from django.db import models


class Listing(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    total_rooms = models.IntegerField()
    location = models.CharField(max_length=100)
    size = models.IntegerField()
    image = models.ImageField()
    

    def __str__(self):
        return self.title
