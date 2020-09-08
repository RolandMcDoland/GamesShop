from django.db import models

class Offer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    release_date = models.DateField()
    developer = models.CharField(max_length=100)
    in_order = models.BooleanField(default=False)
    cover_image = models.CharField(max_length=500)

    def __str__(self):
        return self.name
