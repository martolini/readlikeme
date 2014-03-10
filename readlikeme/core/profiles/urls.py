from django.conf.urls import patterns, url

urlpatterns = patterns('readlikeme.core.profiles.views',
	url(r'^login/$', 'login_view', name='login'),
	url(r'^logout/$', 'logout_view', name='logout'),
	url(r'^signup/$', 'signup_view', name='signup'),
	url(r'^edit_reader/$', 'edit_profile', name='edit_profile'),
	url(r'^(?P<username>\w+)/$', 'profile_view', name='profile'),
)