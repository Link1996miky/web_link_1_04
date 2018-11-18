from django.db import models


# Create your models here.
class user_info_one(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    memo = models.TextField()
