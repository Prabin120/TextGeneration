from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return f"{self.username}"
