from django.db import models
from django.conf import settings
from products.models import Product

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)

    def get_total_cost(self):
        return sum(item.get_total_price() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    selected_color = models.CharField(max_length=50, default='')

    def get_total_price(self):
        color_price = 0
        if self.selected_color == 'oq':
            color_price = self.product.color_white_price
        elif self.selected_color == 'qora':
            color_price = self.product.color_black_price
        elif self.selected_color == 'qizil':
            color_price = self.product.color_red_price
        return self.quantity * (self.product.base_price + color_price)
