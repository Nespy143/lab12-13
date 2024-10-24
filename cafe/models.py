from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_present = models.BooleanField(default=False)  # Присутствует ли в кафе
    is_drinking_coffee = models.BooleanField(default=False)  # Пьет ли кофе

    def __str__(self):
        return self.username
