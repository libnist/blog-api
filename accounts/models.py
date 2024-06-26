from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=100)
    
    def __str__(self) -> str:
        if self.name is None:
            return self.username
        return self.name