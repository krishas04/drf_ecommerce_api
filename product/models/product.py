from django.db import models

from product.models.category import Category

class Product(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  stock = models.PositiveIntegerField()
  image = models.ImageField(upload_to='products/', blank=True, null=True)
  category = models.ForeignKey(
    Category,
    on_delete=models.CASCADE,
    related_name='products'
)

  @property
  def in_stock(self):
      return self.stock > 0
    
  def __str__(self):
      return self.name