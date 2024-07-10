from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    last_login = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.username
