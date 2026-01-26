import uuid
from django.db import models
from django.conf import settings

from core.models.abstract_base_model import AbstractBaseModel
from product.models.product import Product

class Order(AbstractBaseModel):
  class StatusChoices(models.TextChoices):
    PENDING = "Pending"   
    CONFIRMED = "Confirmed"
    CANCELED = "Canceled"

  order_id= models.UUIDField(primary_key=True, default=uuid.uuid4)
  user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  status=models.CharField(max_length=9,choices=StatusChoices.choices, default=StatusChoices.PENDING)
  products=models.ManyToManyField(Product, through="OrderItem", related_name="orders")

  def __str__(self):
    return f"Order{self.order_id} by {self.user.username}"
  
  