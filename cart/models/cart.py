import uuid
from django.db import models
from core.models.abstract_base_model import AbstractBaseModel
from product.models.product import Product
from django.conf import settings

class Cart(AbstractBaseModel):
  cart_id=models.UUIDField(primary_key=True,default=uuid.uuid4)
  user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
  products=models.ManyToManyField(Product, through="CartItem",related_name="carts")

  def __str__(self):
    return f"Cart {self.cart_id} of {self.user.username}"