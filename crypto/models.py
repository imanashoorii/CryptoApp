from django.db import models

# Create your models here.


class Crypto(models.Model):
    name = models.CharField(max_length=200)
    image = models.URLField(max_length=200)
    current_price = models.IntegerField()
    market_cap_rank = models.IntegerField()
    market_cap = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['market_cap_rank']