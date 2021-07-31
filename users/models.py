from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True)
    # age = models.PositiveIntegerField(verbose_name='возраст')

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(auto_now_add=True, null=True)

    def is_activation_key_expired(self):
        if datetime.now() < self.activation_key_created + timedelta(hours=48):
            return False
        return True