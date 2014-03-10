from django.conf.urls import patterns, url

urlpatterns = patterns('readlikeme.app.reader.views',
	url(r'^$', 'frontpage', name='frontpage'),
	url(r'^post_article/$', 'post_article', name='post_article'),
	url(r'^search/$', 'search_view', name="search")
)