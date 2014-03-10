from django.db import models
from readlikeme.core.profiles.models import User

class Article(models.Model):
	url = models.CharField(max_length=140)
	author = models.ForeignKey(User, related_name="articles")