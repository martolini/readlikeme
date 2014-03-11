from django.db import models
from django.contrib.auth.models import AbstractUser


class Reader(AbstractUser):
	followers = models.ManyToManyField('self', related_name='following', symmetrical=False, blank=True)
	bio = models.CharField(max_length=200, blank=True, default="")