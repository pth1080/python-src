import binascii
import hashlib
import os

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=12, null=False, blank=False, default='')
    full_name = models.CharField(max_length=128, blank=True, null=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'auth_user'

