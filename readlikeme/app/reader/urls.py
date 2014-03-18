from django.conf.urls import patterns, url, include

ajax_patterns = patterns('readlikeme.app.reader.ajax', 
	url(r'^ajax/article/delete/$', 'delete_article', name='delete_article'),
)

view_patterns = patterns('readlikeme.app.reader.views',
	url(r'^$', 'frontpage', name='frontpage'),
	url(r'^post_article/$', 'post_article', name='post_article'),
	url(r'^search/$', 'search_view', name="search"),
)

urlpatterns = ajax_patterns + view_patterns