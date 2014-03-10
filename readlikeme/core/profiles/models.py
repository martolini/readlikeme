from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	followers = models.ManyToManyField('self', related_name='followees', symmetrical=False, blank=True)