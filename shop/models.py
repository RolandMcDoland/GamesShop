from django.db import models

class Offer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    developer = models.CharField(max_length=100)

    def __str__(self):
        return self.name
