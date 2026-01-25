from django.db import models
from django.conf import settings

class Profile(models.Model):
  user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name="profile")
  phone_number=models.CharField(max_length=15, blank=True, null=True)
  address=models.TextField(blank=True,null=True)
  city=models.TextField(max_length=100,blank=True,null=True)
  country=models.TextField(max_length=100,blank=True,null=True)
  profile_picture=models.ImageField(upload_to="profile_pic/",blank=True,null=True)

  def __str__(self):
    return f"Profile of {self.user.username}"