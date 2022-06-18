from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Profile(AbstractUser):
    # Holds the user's bio
    bio = models.CharField(max_length=300, blank=True, null=True)

