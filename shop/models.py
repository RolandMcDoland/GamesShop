from django.db import models

class Offer(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=10, default="199,99zł")
    release_date = models.DateField()
    developer = models.CharField(max_length=100)
    in_order = models.BooleanField(default=False)
    cover_image = models.CharField(max_length=500, default="https://store-images.s-microsoft.com/image/apps.28990.69531514236615003.8f0d03d6-6311-4c21-a151-834503c2901a.d629260e-2bc4-4588-950c-f278cbc22a64")

    def __str__(self):
        return self.name
