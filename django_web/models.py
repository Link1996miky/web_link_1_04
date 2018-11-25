from django.db import models


# Create your models here.

class user_info_one(models.Model):
    man = "男"
    women = "女"
    sex_choices = (
        (man, "男"),
        (women, "女"),
    )

    user_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    memo = models.TextField(blank=True)
    sex = models.CharField(
        max_length=2,
        choices=sex_choices,
        default=man,
    )

    def __str__(self):
        return self.user_id
