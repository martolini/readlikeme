from django.db import models
from django.contrib.auth.models import AbstractUser


class Reader(AbstractUser):
	followers = models.ManyToManyField('self', related_name='followees', symmetrical=False, blank=True)
	bio = models.TextField(max_length=200)