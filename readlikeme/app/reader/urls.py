from django.conf.urls import patterns, url

urlpatterns = patterns('readlikeme.app.reader.views',
	url(r'^$', 'frontpage', name='frontpage'),
)