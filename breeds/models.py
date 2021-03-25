from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class Breeds(models.Model):
  purchaser = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=64)
  description = models.TextField(default='')
  height = models.IntegerField('Height in inches')
  weight = models.IntegerField('Weight in pounds')

  def __str__(self):
    return self.name


