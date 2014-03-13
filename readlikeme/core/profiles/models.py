from django.db import models
from django.contrib.auth.models import AbstractUser


class Reader(AbstractUser):
	followers = models.ManyToManyField('self', related_name='following', symmetrical=False, blank=True)
	bio = models.CharField(max_length=200, blank=True, default="")
	avatar = models.ImageField(upload_to='avatars/', default='avatars/no-img.png')


	def save(self, *args, **kwargs):
		try:
			this = Reader.objects.get(id=self.id)
			if this.avatar != self.avatar:
				this.avatar.delete(save=False)
		except:
			pass
		super(Reader, self).save(*args, **kwargs)