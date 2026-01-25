from django.db import models

from orders.models.orders import Order
from product.models.product import Product

class OrderItem(models.Model):
  order=models.ForeignKey(Order,on_delete=models.CASCADE)
  product=models.ForeignKey(Product,on_delete=models.CASCADE)
  quantity=models.PositiveIntegerField()

  @property
  def item_subtotal(self):
    return self.product.price * self.quantity
  
  def __str__(self):
    return f"{self.quantity} x {self.product.name} in order {self.order.order_id}"