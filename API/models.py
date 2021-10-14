from django.db import models

class productos(models.Model):
    name = models.CharField(max_length=50, blank=False)
    price = models.FloatField(blank=False)
    description = models.CharField(max_length=80, blank=False)
    created = models.IntegerField(blank=False)
    updated = models.DateField(blank=False)

    def __str__(self):
        return self.name
