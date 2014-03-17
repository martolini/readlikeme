from django.db import models
from readlikeme.core.profiles.models import Reader
from readlikeme.app.viewcount.models import ViewCount
from urllib2 import urlopen, Request
from BeautifulSoup import BeautifulSoup
import re
from django.contrib.contenttypes import generic
from paypal.standard.ipn.signals import payment_was_successful, payment_was_flagged, payment_was_refunded, payment_was_reversed


class Article(models.Model):
	url = models.URLField()
	title = models.CharField(max_length=200, blank=True, null=True)
	description = models.CharField(max_length=300, blank=True, null=True)
	author = models.ForeignKey(Reader, related_name="articles")
	posted_at = models.DateTimeField(auto_now_add=True)
	viewcount = generic.GenericRelation(ViewCount)

	def save(self):
		if self.id:
			same_articles = Article.objects.filter(url=self.url)
		else:
			same_articles = Article.objects.filter(url=self.url).exclude(id=self.id)
		if len(same_articles) > 0:
			article = same_articles[0]
			self.title = article.title
			self.description = article.description
		else:
			self.title, self.description = self.get_title_and_description(self.url)
		super(Article, self).save()


	def get_title_and_description(self, url):
		hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		'Accept-Encoding': 'none',
		'Accept-Language': 'en-US,en;q=0.8',
		'Connection': 'keep-alive'
		}
		req = Request(url, headers=hdr)
		try:
			html = urlopen(req).read()
		except:
			return '', ''
		soup = BeautifulSoup(html)
		try:
			description = soup.findAll('meta', attrs={'name': re.compile("^description$", re.I)})[0]['content']
		except:
			description = ""

		if len(description) > 160:
			description = description[:160]

		try:
			title = soup.title.string
		except:
			title = ""
		return title, description

	def __unicode__(self):
		return self.url


def show_me_the_money(sender, **kwargs):
	Article(url="http://google.no", author=Reader.objects.all()[0]).save()

payment_was_reversed.connect(show_me_the_money)
payment_was_refunded.connect(show_me_the_money)
payment_was_successful.connect(show_me_the_money)
payment_was_flagged.connect(show_me_the_money)
