from django.db import models

class Category(models.Model):
  name= models.CharField(max_length=100, unique=True)
  slug=models.SlugField(max_length=100, unique=True)
  description=models.TextField(blank=True,null=True)
  is_active=models.BooleanField(default=True)


  class Meta:
    verbose_name_plural="Categories"

  def __str__(self):
    return self.name