from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name
