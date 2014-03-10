from django.conf.urls import patterns, url

urlpatterns = patterns('readlikeme.core.profiles.views',
	url(r'^login/$', 'login_view', name='login'),
	url(r'^logout/$', 'logout_view', name='logout'),
	url(r'^signup/$', 'signup_view', name='signup'),
)