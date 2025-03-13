from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    photo_url = models.URLField(blank=True)

    def __str__(self):
        return self.username
