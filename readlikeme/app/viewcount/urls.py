from django.conf.urls import patterns, url

ajax_patterns = patterns('readlikeme.app.viewcount.ajax',
	url(r'^ajax/view/$', 'view_count', name='view_count'),
)

urlpatterns = ajax_patterns
