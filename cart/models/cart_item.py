from django.db import models

from cart.models.cart import Cart
from product.models.product import Product

class CartItem(models.Model):
  cart=models.ForeignKey(Cart,on_delete=models.CASCADE, related_name='cart_items')
  product=models.ForeignKey(Product,on_delete=models.CASCADE)
  quantity=models.PositiveIntegerField()

  class Meta:
    unique_together=("cart","product")

  def __str__(self):
    return f"{self.quantity} {self.product.name}"