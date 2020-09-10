from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=False)
    price = models.FloatField(blank=True)
    image = models.ImageField(blank=True)
    release_date = models.DateField(blank=True)
    lte_exists = models.BooleanField(blank=True)
    slug = models.CharField(max_length=150)

    # def __str__(self):
    #     return f'{self.name}, {self.price}'