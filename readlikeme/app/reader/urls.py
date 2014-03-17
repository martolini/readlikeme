from django.conf.urls import patterns, url, include

ajax_patterns = patterns('readlikeme.app.reader.ajax', 
	url(r'^ajax/article/delete/$', 'delete_article', name='delete_article'),
)

view_patterns = patterns('readlikeme.app.reader.views',
	url(r'^$', 'frontpage', name='frontpage'),
	url(r'^post_article/$', 'post_article', name='post_article'),
	url(r'^search/$', 'search_view', name="search"),
	url(r'^credits/purchase/$', 'purchase_credits', name='purchase_credits'),
	url(r'^something/paypal/', include('paypal.standard.ipn.urls')),
	url(r'^credits/return/$', 'purchase_return', name='purchase_return'),
	url(r'^credits/cancel/$', 'purchase_cancel', name='purchase_cancel'),
)

urlpatterns = ajax_patterns + view_patterns