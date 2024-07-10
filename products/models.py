from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    color_white_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    color_black_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    color_red_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.title
